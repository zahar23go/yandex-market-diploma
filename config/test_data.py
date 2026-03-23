class TestData:
    SEARCH_QUERIES = {
        "single_word": "шоколад",
        "partial": "шоко",
        "phrase": "темный шоколад",
        "with_number": "iPhone 14",
        "non_existent": "Топливный насос",
        "complaint": "Сливки испорчены",
        "empty": "",
        "special_chars": "шоколад?",
        "location_query": "где купить шоколад"
    }
    
    EXPECTED_MESSAGES = {
        "not_found": "По запросу '{query}' ничего не найдено",
        "empty_search": "Введите запрос для поиска"
    }
