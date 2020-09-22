import math
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--type', help='"=annuity" or "=diff"')
parser.add_argument('--principal', type=int)
parser.add_argument('--payment', type=int)
parser.add_argument('--periods', type=int)
parser.add_argument('--interest', type=float)
args = parser.parse_args()

if len(sys.argv) < 4 or args.type != ('diff' and 'annuity'):
    print('Incorrect parameters')

def overpayment(total_paid, principal):
    sum_paid = total_paid - principal
    print(f'Overpayment = {sum_paid}')
    return sum_paid


def diff_payment(principal, period, interest):
    total_payment = 0
    for i in range(1, period + 1):
        nominal_i = (interest / 100) / (12 * 1)
        dm = math.ceil((principal / period) + nominal_i * (principal - (principal * (i - 1)) / period))
        print('Month ' + str(i) + ': paid out ' + str(dm))
        total_payment += dm
    return total_payment


def x_periods(principal, payment, interest):
    nominal_i = (interest / 100) / 12
    periods = math.ceil(math.log((payment / (payment - nominal_i * principal)), 1 + nominal_i))
    conversion_year = periods // 12
    conversion_month = math.ceil(periods % 12)
    total_payment = payment * periods
    if conversion_month == 12 or conversion_month == 0:
        print(f'You need {str(int(conversion_year))} years to repay this credit!')
    else:
        print(f'You need {str(int(conversion_year))} year and {str(conversion_month)} months to repay this credit!')
    return total_payment


def x_payment(principal, periods, interest):
    nominal_i = (interest / 100) / 12
    annuity = math.ceil(principal * ((nominal_i * ((1 + nominal_i) ** periods)) / (((1 + nominal_i) ** periods) - 1)))
    total_payment = periods * annuity
    print(f'Your annuity payment = {annuity}!')
    return total_payment


def x_principal(payment, period, interest):
    nominal_i = (interest / 100) / (12 * 1)
    principal = math.ceil(payment / ((nominal_i * ((1 + nominal_i) ** period)) / (((1 + nominal_i) ** period) - 1)))
    print(f'Your credit principal = {principal}!')
    return principal


if args.type == 'diff':
    overpayment(diff_payment(args.principal, args.periods, args.interest), args.principal)
else:
    if not args.periods:
        overpayment(x_periods(args.principal, args.payment, args.interest), args.principal)
    elif not args.payment:
        overpayment(x_payment(args.principal, args.periods, args.interest), args.principal)
    elif not args.principal:
        total = args.periods * args.payment
        print(f'Overpayment = {total - x_principal(args.payment, args.periods, args.interest)}')