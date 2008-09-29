from satchmo.configuration import config_get_group
from satchmo.payment.views import confirm, payship
    
def pay_ship_info(request):
    return payship.credit_pay_ship_info(request, config_get_group('PAYMENT_CYBERSOURCE'))
    
def confirm_info(request):
    return confirm.credit_confirm_info(request, config_get_group('PAYMENT_CYBERSOURCE'))
