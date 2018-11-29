import argschema


class InputSchema(argschema.schemas.LogSchema):
    a = argschema.fields.String(required=True, help='a string field')
    b = argschema.fields.String(help='another string field')
    c = argschema.fields.String(default='hello world', help='yasf')


# class OutputSchema(argschema.schemas.DefaultSchema):
#     pass


def main():

    parser = argschema.ArgSchemaParser(
        schema_type=InputSchema,
        output_schema_type=InputSchema
    )

    parser.sink(parser.args)


if __name__ == '__main__':
    main()