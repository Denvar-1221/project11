from django.shortcuts import render
from django.shortcuts import redirect
from .models import products_data
def homepage(request):
    product=products_data.objects.all()
    return render(request,'homepage.html',{'product':product})
def add_product(request):
    if request.method=='GET':
        return render(request,'add_product.html')
    else:
        products_data(
        product_id=request.POST.get('pid'),
        product_name=request.POST.get('pname'),
        product_cost=request.POST.get('pcost'),
        product_description=request.POST.get('pdescription'),
        ).save()
        return redirect('homepage')
def update_product(request,id):
    products=products_data.objects.get(id=id)
    if request.method=='GET':
        return render(request,'update_student.html',{'student':student})
    else:
        student.first_name=request.POST.get('fname')
        student.last_name=request.POST.get('lname')
        student.course=request.POST.get('course')
        student.fee=request.POST.get('fee')
        student.location=request.POST.get('location')
        student.save()
        return redirect('homepage')

def delete_student(request,id):
    student=students_data.objects.get(id=id)
    student.delete()
    return redirect('homepage')
