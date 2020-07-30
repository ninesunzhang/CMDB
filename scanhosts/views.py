from django.shortcuts import render
from django.http import HttpResponse
from .models import Server
from .utils import get_active_hosts,is_ssh_up,login_ssh_key
from devops.settings import commands

def hostscan(request):
    print(request.method)
    if request.method == 'POST':
#        print(request.POST)
        scanhosts = request.POST.get('scanhosts').split(',')
#        return HttpResponse('upload scan host')
        servers = []
        for scanhost in scanhosts:
            print("scaning %s now" %(scanhost))
            active_hosts=get_active_hosts(scanhost)
            for activehost in active_hosts:
                if is_ssh_up(activehost):
                    server = Server()
                    server.IP = activehost
                    for command_name,command in commands.items():
                        result = login_ssh_key(hostname=activehost,command=command)
                        setattr(server,command_name,result)
                    server.save()
                    servers.append(server)
        return render(request,"hostscan.html",{'servers':servers})
        #return HttpResponse(server)
    return render(request,'hostscan.html')
