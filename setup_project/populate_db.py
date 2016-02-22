__author__ = 'rene_esteves'

def populate_ordered(input):
    serie = add_serie('ordered-10000')
    for p in range(input):
        add_datum(p, serie)

def add_serie(name):
    serie = Serie(serie_text=name)
    serie.save()
    print ("serie = " + str(serie));
    return serie

def add_datum(value, serie):
    datum = Datum(datum_value=value,serie=serie)
    datum.save()
    print ("datum = " + str(datum));

if __name__ == '__main__':
    #Import default
    import django
    django.setup()
    from data_structure.models import Serie, Datum
    #Execution here
    print ("Starting population database script...")
    populate_ordered(10001)

    print ("Finishing population database script...")