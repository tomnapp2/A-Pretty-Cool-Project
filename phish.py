def phish(**kwargs):
    if len(kwargs):
        for i in kwargs:
            print('Mr. {} plays {}'.format(i, kwargs[i]))
    else: print('Play me a Twiddle song.')

x = {'Jon': 'Drum', 'Trey': 'Guitar', 'Page': 'Keys', 'Mike': 'Bass'}
phish(**x)
