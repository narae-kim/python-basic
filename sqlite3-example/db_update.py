import sqlite3


def main():
    conn = sqlite3.connect('zoo_db')
    curs = conn.cursor()

    invalid = True
    while invalid:
        animal = input('Animal name?')
        if type(animal) == str and len(animal) > 0:
            invalid = False
    invalid_count = True
    while invalid_count:
        count = input('How many?')  # input ALWAYS returns a string!!!
        count_int = int(float(count))  # cast the string to an integer
        if type(count_int) is int and count_int >= 0:
            invalid_count = False
    invalid_cost = True
    while invalid_cost:
        cost = input('How much?')  # input ALWAYS returns a string!!!
        cost_float = float(cost)
        if type(cost_float) is float and cost_float >= 0.0:
            invalid_cost = False

    # conventionally capitalize SQL key words
    update_count_statement = '''
    UPDATE zoo
    SET count = {}
    WHERE animal IS "{}"
    '''.format(count, animal)  # inject user values into the SQL statement. Double-quote for SQL.

    update_cost_statement = '''
    UPDATE zoo
    SET cost = {}
    WHERE animal IS "{}"
    '''.format(cost_float, animal)

    # use '?' as a placeholder in SQL statements
    insert_statement = '''
    INSERT INTO zoo
    VALUES (?, ?, ?)
    '''

    try:
        # curs.execute(update_cost_statement)
        curs.execute(insert_statement,
                     (animal, count_int, cost_float))  # replace the '?' placeholders with actual values
        conn.commit()
    except Exception as e:
        print('There was a problem: {}'.format(e))
    finally:
        conn.close()  # always make sure the connection is closed


if __name__ == '__main__':
    main()
