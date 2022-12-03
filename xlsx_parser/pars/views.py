from django.shortcuts import render

from pars.models import Table, BaseStat, DataRow


def mainpage_views(request):
    stat_data_qoil_fact = ''
    stat_data_qliq_fact = ''
    stat_data_qliq_forecast = ''
    stat_data_qoil_forecast = ''
    current_table = ''
    if request.method == 'POST' and request.FILES['tablefile']:
        tablefile = request.FILES['tablefile']
        table_name = Table.pars_table(table_file=tablefile)
        stat_data_qliq_fact = BaseStat.qliq_stat_fact(table_name)
        stat_data_qoil_fact = BaseStat.qoil_stat_fact(table_name)
        stat_data_qliq_forecast = BaseStat.qliq_stat_forecast(table_name)
        stat_data_qoil_forecast = BaseStat.qoil_stat_forecast(table_name)
        current_table = DataRow.objects.filter(table=Table.objects.filter(name=table_name)[0])



    last_tables = Table.objects.all()
    template_name = 'base_template.html'
    context = {
        'current_table': current_table,
        'stat_data_qliq_fact': stat_data_qliq_fact,
        'stat_data_qoil_fact': stat_data_qoil_fact,
        'stat_data_qliq_forecast': stat_data_qliq_forecast,
        'stat_data_qoil_forecast': stat_data_qoil_forecast,
        'last_tables': last_tables,
    }

    return render(request, template_name, context)

def show_table(request,table_id):
    table = Table.objects.filter(pk=table_id)
    current_table = DataRow.objects.filter(table=table[0])

    stat_data_qliq_fact = BaseStat.qliq_stat_fact(table_id)
    stat_data_qoil_fact = BaseStat.qoil_stat_fact(table_id)
    stat_data_qliq_forecast = BaseStat.qliq_stat_forecast(table_id)
    stat_data_qoil_forecast = BaseStat.qoil_stat_forecast(table_id)

    template_name = 'show_table_template.html'
    context = {
        'table_name': table[0].name,
        'current_table': current_table,
        'stat_data_qliq_fact': stat_data_qliq_fact,
        'stat_data_qoil_fact': stat_data_qoil_fact,
        'stat_data_qliq_forecast': stat_data_qliq_forecast,
        'stat_data_qoil_forecast': stat_data_qoil_forecast,
    }
    return render(request, template_name, context)
