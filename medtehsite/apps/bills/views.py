﻿from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Bill
from .forms import BillForm


def bill_list(request):

    display = request.GET.get('display')
    if display == 'all':
        bills = Bill.objects.all()
    elif display == 'supply':
        bills = Bill.objects.filter(supply='Да')
    else:
        bills = Bill.objects.filter(supply='Нет')

    return render(request, 'bills/bill_list.html', {'bills': bills})


def bill_detail(request, pk):

    if request.method == 'POST':
        bill = Bill.objects.get(pk=pk)
        bill.supply = 'Да'
        bill.supply_date = timezone.now()
        bill.save()
    else:
        """
        Обрабатываю "пустую" страницу
        """
        pk_last = request.META.get('HTTP_REFERER', '')
        if pk_last:
            pk_last = pk_last.split('/')[-1]
        else:
            pk_last = Bill.objects.all().last().pk

        try:
            bill = Bill.objects.get(pk=pk)
        except Bill.DoesNotExist:
            return render(request, 'bills/bill_not_found.html', {'pk': pk_last})

    return render(request, 'bills/bill_detail.html', {'bill': bill})


def bill_new(request):

    if request.method == 'POST':
        form = BillForm(request.POST)
        if form.is_valid():
            print('form is valid')
            bill = form.save()
            bill.save()
            return redirect('bills:bill_detail', pk=bill.pk)
        else:
            print('form not valid')
            print('------------')
            # print(form)
            print(dir(form))
            print('------------')
            print('------------')
            print(form.data)
            print(form['product'])
            print(form['supply'])
            print('------------')
    else:
        form = BillForm()

    return render(request, 'bills/bill_new.html', {'form': form})


def bill_edit(request, pk):

    bill = Bill.objects.get(pk=pk)
    print('bill_product =', bill.product)
    if request.method == 'POST':
        form = BillForm(request.POST, instance=bill)
        print('form_new=', form.instance)
        print('================================================')
        if form.instance.supply == "Да":
            print('--- supply == Да ---')
            bill.supply_date = timezone.now()
        elif form.instance.supply == "Нет":
            print('--- supply == Нет ---')
            bill.supply_date = None
        print('================================================1')
        for item in form:
            print(item)
        print('================================================1')
        print('product =', form.instance.product)
        print('supplier =', form.instance.supplier)
        print('clinic =', form.instance.clinic)
        print('device =', form.instance.device)
        print('engineer =', form.instance.engineer)
        print('supply =', form.instance.supply)
        print('================================================2')

        if form.is_valid():
            # bill = form.save()
            print('form = ', form.instance.product)
            bill.product = form.instance.product
            print('bill = ', bill.product)
            bill.save(update_fields=['product'])
            print('--- form is valid ---')
            return redirect('bills:bill_detail', pk=bill.pk)
        print('--- form not valid ---')
        print(form.errors.as_data())
    else:
        # print('===')
        # print(bill)
        # print('===')
        form = BillForm(instance=bill)
    print('In bill edit')
    print('===')

    return render(request, 'bills/bill_edit.html', {'form': form, 'bill': bill})


def test(request):
    return render(request, 'test/test.html', )


def test2(request):
    bill = Bill.objects.get(pk=2)
    form = BillForm(instance=bill)
    # if request.method == 'POST':
    #     form = BillForm(request.POST, instance=bill)
    #     if form.instance.supply == "Да":
    #         bill.supply_date = timezone.now()
    #     elif form.instance.supply == "Нет":
    #         bill.supply_date = None
    #
    #     if form.is_valid():
    #         bill = form.save()
    #         bill.save()
    #         return redirect('bills:bill_detail', pk=bill.pk)
    # else:
    #     form = BillForm(instance=bill)

    return render(request, 'test/test2.html', {'form': form, 'bill': bill})


def test3(request):
    return render(request, 'test/test3.html')




# Старая функция bill_edit
#
# def bill_edit(request, pk):
#
#     # bill = get_object_or_404(Bill, pk)
#     bill = Bill.objects.get(pk=pk)
#     # print('pk=', pk)
#     # print(bill)
#     # print('--- 1 ---')
#     if request.method == 'POST':
#         # print('--- 2 ---')
#         form = BillForm(request.POST, instance=bill)
#         if form.instance.supply == "Да":
#             print('--- supply == Да ---')
#             bill.supply_date = timezone.now()
#         elif form.instance.supply == "Нет":
#             print('--- supply == Нет ---')
#             bill.supply_date = None
#
#         print('supply =', form.instance.supply)
#
#         if form.is_valid():
#             # bill = form.save()
#             print('form = ', form.instance.product)
#             bill.product = form.instance.product
#             # bill.product = form.
#             print('bill = ', bill.product)
#             bill.save(update_fields=['product'])
#             print('--- form is valid ---')
#             return redirect('bills:bill_detail', pk=bill.pk)
#         print('--- form not valid ---')
#         print(form.errors.as_data())
#     else:
#         # print('===')
#         # print(bill)
#         # print('===')
#         form = BillForm(instance=bill)
#         # print('product =', form)
#     print('In bill edit')
#     print('===')
#     # print(bill)
#     # print('===')
#     # print(form)
#     # print('===')
#
#     return render(request, 'bills/bill_edit.html', {'form': form, 'bill': bill})


