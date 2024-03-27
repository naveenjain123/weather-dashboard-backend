from marshmallow import Schema, fields


class SearchReportApiSchema(Schema):
    # The above class defines the schema for a search report API, including various fields such as query,
    # uid, start_page, destination, destination_type, device, ip, and add_question_status.
    query = fields.String(required=True)
    uid = fields.Integer()
    start_page = fields.String(required=True)
    destination = fields.String(required=True)
    destination_type = fields.String()
    device = fields.String()
    ip = fields.String()
    add_question_status = fields.Integer()
