import json


class PartnerContent:
    def __init__(self):
        self.title = None
        self.description = None

    def update(self, update_json: json) -> bool:
        flag = False
        try:
            if self.title != update_json['title']:
                self.title = update_json['title']
                flag = True
        except KeyError:
            pass

        try:
            if self.description != update_json['description']:
                self.description = update_json['description']
                flag = True
        except KeyError:
            pass

        return flag

    def get_json(self) -> dict:
        result = {}
        if self.title:
            result['title'] = self.title
        if self.description:
            result['description'] = self.description
        return result


class Offer:
    def __init__(self, inp_id: str):
        self.id = inp_id
        self.data = {'price': None, 'stock_count': None, 'partner_content': PartnerContent()}

    def update(self, update_json: json) -> bool:
        flag = False
        try:
            if self.data['price'] != update_json['price']:
                self.data['price'] = update_json['price']
                flag = True
        except KeyError:
            pass

        try:
            if self.data['stock_count'] != update_json['stock_count']:
                self.data['stock_count'] = update_json['stock_count']
                flag = True
        except KeyError:
            pass

        try:
            pc_update = update_json['partner_content']
            flag = flag or self.data['partner_content'].update(pc_update)
        except KeyError:
            pass
        return flag

    def build_response(self, response_fields: list[str]) -> dict:
        result = dict()
        result['id'] = self.id
        for field in response_fields:
            if field == 'partner_content':
                result[field] = self.data[field].get_json()
            elif self.data[field] is not None:
                result[field] = self.data[field]
        return result


class Subscriber:
    def __init__(self, trigger: list[str], shipment: list[str]):
        self.trigger = trigger
        self.shipment = shipment
        self.response_fields = self.trigger + list(set(self.shipment)-set(self.trigger))

    def is_interested(self, inp_json: json) -> bool:
        for i in self.trigger:
            if i in inp_json.keys():
                return True
        return False

    def build_response(self, inp_json: json, offer: Offer) -> str:
        result = dict()
        result['trace_id'] = inp_json['trace_id']
        result['offer'] = offer.build_response(self.response_fields)
        return json.dumps(result, separators=(',', ':'))


if __name__ == "__main__":
    n, m = [int(i) for i in input().split()]
    subs = []
    offers = {}
    for i in range(n):
        current_sub = input().split()
        a, b = int(current_sub[0]), int(current_sub[1])
        subs.append(Subscriber(current_sub[2:2 + a], current_sub[2 + a:]))
    for i in range(m):
        inp = json.loads(input())
        try:
            updated_offer = offers[int(inp['offer']['id']) - 1]
        except KeyError:
            offers[int(inp['offer']['id']) - 1] = Offer(inp['offer']['id'])
            updated_offer = offers[int(inp['offer']['id']) - 1]

        update_flag = updated_offer.update(inp['offer'])
        if not update_flag:
            continue
        for sub in subs:
            if sub.is_interested(inp['offer']):
                print(sub.build_response(inp, updated_offer))
