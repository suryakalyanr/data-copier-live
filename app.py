import sys
from loguru import logger

from util import get_tables, load_db_details
from read import read_table
from write import load_table


def main():
    """The usage is :- python app.py env table_list """
    print ("The parameters are:",sys.argv)
    env = sys.argv[1]
    a_tables = sys.argv[2]
    logger.add("logs/data-copier.info",
               rotation="1 KB",
               retention="10 days",
               level="INFO"
               )
    logger.add("logs/data-copier.err",
               rotation="1 KB",
               retention="10 days",
               level="ERROR"
               )

    db_details = load_db_details(env)
    print (db_details)
    logger.debug(db_details)
    tables = get_tables('table_list', a_tables)
    print (tables)
    logger.debug(tables)

    for table_name in tables['table_name']:
        logger.info(f'reading data for {table_name}')
        data, column_names = read_table(db_details, table_name)
        logger.debug(f'Data is: {data}')
        logger.debug(f"Column names are:{column_names}")
        logger.info(f'loading data for {table_name}')
        load_table(db_details, data, column_names, table_name)


def truncate_tables(env, tables):
    db_details = load_db_details(env)



if __name__ == '__main__':
    main()
