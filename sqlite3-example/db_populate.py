import sqlite3


def main():
    # a structure for the data members to be added to the db
    animal_t = ({'animal': 'Anaconda', 'count': 1, 'cost': 120.99},
                {'animal': 'Bear', 'count': 5, 'cost': 32.56},
                {'animal': 'Camel', 'count': 120, 'cost': 120.99},
                {'animal': 'Deer', 'count': 32, 'cost': 12.99},
                {'animal': 'Elephant', 'count': 7, 'cost': 73.82})

    conn = sqlite3.connect('zoo_db')
    curs = conn.cursor()
    # iterate over our structure
    # use '?' as a placeholder in SQL statements
    statement = '''
        INSERT INTO zoo
        VALUES (?, ?, ?)
        '''
    for item in animal_t:
        try:
            curs.execute(statement, (
            item['animal'], item['count'], item['cost']))  # replace the '?' placeholders with actual values
            conn.commit()
        except Exception as e:
            print('There was a problem: {}'.format(e))
        finally:
            pass
    conn.close()


if __name__ == '__main__':
    main()
