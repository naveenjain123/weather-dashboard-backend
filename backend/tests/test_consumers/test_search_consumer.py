from backend.consumers.entity_to_search_index_consumers import (
    ArticleToSearchIndexConsumer,
    CollegeToSearchIndexConsumer,
    EbooksToSearchIndexConsumer,
    ExamToSearchIndexConsumer,
    KeywordsSynonymsToSearchIndexConsumer,
    KeywordToSearchIndexConsumer,
    PredictorToSearchIndexConsumer,
    SchoolToSearchIndexConsumer,
    SynonymsToSearchIndexConsumer,
)


def test_ebook_search_consumer():
    msg = {
        "database": "django360",
        "table": "ebooks",
        "type": "update",
        "ts": 1700125334,
        "xid": 73268941,
        "commit": True,
        "data": {
            "id": 1,
            "type_of_entity": 1,
            "name": "North Eastern Regional Institute of Science and Technology, Nirjuli",
            "short_name": "NERIST Nirjuli",
        },
        "old": {"adm_client": 0},
    }
    assert (EbooksToSearchIndexConsumer().consume(msg)) == True


def test_college_search_consumer():
    msg = {
        "database": "django360",
        "table": "colleges",
        "type": "update",
        "ts": 1700125334,
        "xid": 73268941,
        "commit": True,
        "data": {
            "id": 1,
            "type_of_entity": 1,
            "name": "North Eastern Regional Institute of Science and Technology, Nirjuli",
            "short_name": "NERIST Nirjuli",
        },
        "old": {"adm_client": 0},
    }
    assert (CollegeToSearchIndexConsumer().consume(msg)) == True


def test_article_search_consumer():
    msg = {
        "database": "django360",
        "table": "article",
        "type": "update",
        "ts": 1700125334,
        "xid": 73268941,
        "commit": True,
        "data": {
            "id": 1,
            "type_of_entity": 1,
            "name": "North Eastern Regional Institute of Science and Technology, Nirjuli",
            "short_name": "NERIST Nirjuli",
        },
        "old": {"adm_client": 0},
    }
    assert (ArticleToSearchIndexConsumer().consume(msg)) == True


def test_news_search_consumer():
    msg = {
        "database": "django360",
        "table": "schools",
        "type": "update",
        "ts": 1700125334,
        "xid": 73268941,
        "commit": True,
        "data": {
            "id": 1,
            "type_of_entity": 1,
            "name": "North Eastern Regional Institute of Science and Technology, Nirjuli",
            "short_name": "NERIST Nirjuli",
        },
        "old": {"adm_client": 0},
    }
    assert (SchoolToSearchIndexConsumer().consume(msg)) == True


def test_exam_search_consumer():
    msg = {
        "database": "django360",
        "table": "exams",
        "type": "update",
        "ts": 1700125334,
        "xid": 73268941,
        "commit": True,
        "data": {
            "id": 1,
            "type_of_entity": 1,
            "name": "North Eastern Regional Institute of Science and Technology, Nirjuli",
            "short_name": "NERIST Nirjuli",
        },
        "old": {"adm_client": 0},
    }
    assert (ExamToSearchIndexConsumer().consume(msg)) == True


def test_predictor_search_consumer():
    msg = {
        "database": "django360",
        "table": "cnext_product",
        "type": "update",
        "ts": 1700125334,
        "xid": 73268941,
        "commit": True,
        "data": {
            "id": 1,
            "type_of_entity": 1,
            "name": "North Eastern Regional Institute of Science and Technology, Nirjuli",
            "short_name": "NERIST Nirjuli",
        },
        "old": {"adm_client": 0},
    }
    assert (PredictorToSearchIndexConsumer().consume(msg)) == True


def test_keywords_search_consumer():
    msg = {
        "database": "django360",
        "table": "keywords",
        "type": "update",
        "ts": 1700125334,
        "xid": 73268941,
        "commit": True,
        "data": {
            "id": 1,
            "type_of_entity": 1,
            "name": "North Eastern Regional Institute of Science and Technology, Nirjuli",
            "short_name": "NERIST Nirjuli",
        },
        "old": {"adm_client": 0},
    }
    assert (KeywordToSearchIndexConsumer().consume(msg)) == True


def test_keywords_synonyms_search_consumer():
    msg = {
        "database": "django360",
        "table": "keyword_synonyms",
        "type": "update",
        "ts": 1700125334,
        "xid": 73268941,
        "commit": True,
        "data": {
            "id": 1,
            "type_of_entity": 1,
            "name": "North Eastern Regional Institute of Science and Technology, Nirjuli",
            "short_name": "NERIST Nirjuli",
        },
        "old": {"adm_client": 0},
    }
    assert (KeywordsSynonymsToSearchIndexConsumer().consume(msg)) == True


def test_synonyms_search_consumer():
    msg = {
        "database": "django360",
        "table": "synonyms",
        "type": "update",
        "ts": 1700125334,
        "xid": 73268941,
        "commit": True,
        "data": {
            "id": 1,
            "type_of_entity": 1,
            "name": "North Eastern Regional Institute of Science and Technology, Nirjuli",
            "short_name": "NERIST Nirjuli",
        },
        "old": {"adm_client": 0},
    }
    assert (SynonymsToSearchIndexConsumer().consume(msg)) == True
