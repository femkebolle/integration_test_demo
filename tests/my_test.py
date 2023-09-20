
def test_integration(mock_db):
    # Insert data
    insert_data_query = """
    INSERT INTO sample_table (name) VALUES ('Alice'), ('Bob');
    """
    mock_db.execute(insert_data_query)
    mock_db.commit()

    # Retrieve data
    select_data_query = """
    SELECT * FROM sample_table;
    """
    results = mock_db.select_all(select_data_query)

    assert results == [(1, 'Alice'), (2, 'Bob')]


def test_unit():
    assert 1 == 2
