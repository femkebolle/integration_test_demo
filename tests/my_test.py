from src.base_logger import logger


# def test_my_integration(mock_db):
#     logger.debug('Success!')
#     print(type(mock_db))
#
#     create_table_query = """
#     CREATE TABLE IF NOT EXISTS sample_table (
#         id INT AUTO_INCREMENT PRIMARY KEY,
#         name VARCHAR(255) NOT NULL
#     )
#     """
#     mock_db.execute(create_table_query)
#     mock_db.commit()
#
#     # Insert data
#     insert_data_query = """
#     INSERT INTO sample_table (name) VALUES ('Alice'), ('Bob')
#     """
#     mock_db.execute(insert_data_query)
#     mock_db.commit()
#
#     # Retrieve data
#     select_data_query = """
#     SELECT * FROM sample_table
#     """
#     results = mock_db.select_all(select_data_query)
#     print(results)


def test_my_unit():
    logger.info(f'What a great unit test!')
