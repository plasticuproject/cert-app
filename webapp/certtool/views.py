"""Views for certtool app"""
# certtool/views.py

import subprocess
from pathlib import Path
from django.shortcuts import render, redirect, HttpResponse
from .models import Certs
from .forms import CertForm, CertIdsForm

CERT_DIR = Path.cwd() / 'certs'
CWD = Path.cwd()


def about(request):
    """about view"""
    return render(request, 'about.html')


def tool(request):
    """home page view"""
    if not request.user.is_authenticated:
        return redirect('accounts/login')
    form = CertIdsForm(request.POST)
    if request.method == 'POST':
        if 'download_cert' in request.POST:
            cert_id = request.POST.get('download_cert', None)
            return download_cert(cert_id)
        if form.is_valid():
            cert_id = request.POST.get('cert_name', None)
            return read_cert(request, cert_id, form)
    return render(request, 'tool.html', {'form': form})


def read_cert(request, cert_id, form):
    """function for returning cert details"""
    if not request.user.is_authenticated:
        return redirect('accounts/login')
    cert = Certs.objects.get(pk=cert_id)  # pylint: disable=no-member
    bools = {0: 'No', 1: 'Yes'}
    return render(
        request, 'cert_view.html', {
            'cert_id': cert_id,
            'date_added': cert.date_added,
            'applied': bools[cert.applied],
            'date_applied': cert.date_applied,
            'banned': bools[cert.banned],
            'banned_date': cert.banned_date,
            'required_activation': bools[cert.required_activation],
            'currently_used': bools[cert.currently_used],
            'form': form,
            'cert_ip': cert_id.split('-')[0],
        })


def cert_edit(request, cert_id):
    """edit cert view"""
    if not request.user.is_authenticated:
        return redirect('accounts/login')
    name = cert_id.split('-')[0]
    cert = Certs.objects.get(pk=cert_id)  # pylint: disable=no-member
    form = CertForm(instance=cert)
    if request.method == 'POST':
        if 'download_cert' in request.POST:
            cert_id = request.POST.get('download_cert', None)
            return download_cert(cert_id)
        if form.is_valid:
            if 'submit' in request.POST:
                form.save(commit=False)
                new_form = CertIdsForm(request.POST)
                return read_cert(request, cert_id, new_form)
    return render(request, 'cert_edit.html', {'test': name, 'form': form})


def download_cert(cert_id):
    """function to extract and download the cert files"""
    try:
        subprocess.call(
            ['wine', (CERT_DIR / 'proprietary.exe'), (CERT_DIR / cert_id)],
            timeout=5)
    except subprocess.TimeoutExpired:
        pass
    for item in CERT_DIR.iterdir():
        if item.is_dir():
            cert_folder = item.name
    zip_name = cert_folder + '.zip'
    subprocess.Popen([
        'zip',
        '-rj',
        str(CERT_DIR / zip_name),
        str(CERT_DIR / cert_folder),
    ])
    while True:
        try:
            cert_file = open(CERT_DIR / zip_name, 'rb')
            break
        except FileNotFoundError:
            pass
    subprocess.Popen(['rm', '-r', str(CERT_DIR / cert_folder)])
    response = HttpResponse(cert_file, content_type='application/zip')
    response['Content-Disposition'] = f'attachment; filename={zip_name}'
    return response
