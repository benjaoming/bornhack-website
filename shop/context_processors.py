def current_order(request):
    if request.user.is_authenticated():
        order = None
        orders = request.user.orders.filter(finalized=False)

        if orders:
            order = orders[0]

        return {'current_order': order}
    return {}


