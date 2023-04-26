from task3 import Offer
import json


def test1():
    of = Offer()
    assert of.update(json.loads('{"trace_id": "1", "offer": {"id": "1", "price": 9990}}')['offer']) is True
    assert of.update(json.loads('{"trace_id": "1", "offer": {"id": "1", "price": 9990}}')['offer']) is False
    assert of.update(json.loads('{"trace_id": "2", "offer": {"id": "1", "stock_count": 100}}')['offer']) is True

def test_partner_content():
    of = Offer()
    assert of.update(json.loads('{"trace_id": "3", "offer": {"id": "2", "partner_content": {"title": "Backpack"}}}')['offer']) is True
    assert of.update(json.loads('{"trace_id": "5", "offer": {"id": "2", "partner_content": {"description": "Best backpack ever"}}}')['offer']) is True
