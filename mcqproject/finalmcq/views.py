from django.shortcuts import render
from django.shortcuts import render, redirect
import psutil
from .models import network

# Create your views here.
def index_view(request):
    return render(request, 'index.html')


def get_ip_address(request):
    user_ip_address = request.META.get('HTTP_X_FORWARDED_FOR')
    if user_ip_address:
        ip = user_ip_address.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_network_info(request):
    user_ip = get_ip_address(request)

    mac_address = None
    for interface in psutil.net_if_addrs():
        if psutil.net_if_addrs()[interface][0].address:
            mac_address = psutil.net_if_addrs()[interface][0].address
            break

    cpu_count = psutil.cpu_count()
    memory_info = psutil.virtual_memory()
    disk_partitions = psutil.disk_partitions()
    net_io = psutil.net_io_counters()
    net_connections = psutil.net_connections()

    return render(request, "network.html", {
        "user_ip": user_ip,
        "mac_address": mac_address,
        "cpu_count": cpu_count,
        "memory_info": memory_info,
        "disk_partitions": disk_partitions,
        "net_io": net_io,
        "net_connections": net_connections,
    })


# -------insert data in database -----
def start_exam(request):
    if request.method == 'POST':
        user_ip = request.POST.get('user_ip')
        mac_address = request.POST.get('mac_address')
        cpu_count = request.POST.get('cpu_count')
        total_memory = request.POST.get('total_memory')
        available_memory = request.POST.get('available_memory')
        used_memory = request.POST.get('used_memory')
        free_memory = request.POST.get('free_memory')
        bytes_sent = request.POST.get('bytes_sent')
        bytes_received = request.POST.get('bytes_received')
        packets_sent = request.POST.get('packets_sent')
        packets_received = request.POST.get('packets_received')

        # Save the data to the database
        network.objects.create(user_ip=user_ip, mac_address=mac_address, cpu_count=cpu_count, total_memory=total_memory,
                               available_memory=available_memory, used_memory=used_memory, free_memory=free_memory,
                               bytes_sent=bytes_sent, bytes_received=bytes_received, packets_sent=packets_sent,
                               packets_received=packets_received)

        # Redirect to the exam page

    # Fetch all data from the database
    all_network_data = network.objects.all()

    return render(request, 'exam.html', {'all_network_data': all_network_data})


# -------fetch all data from database ----


# ---delete all data ----
def delete_data(request):
    # Delete all data from the network table
    network.objects.all().delete()

    return redirect('start_exam')
