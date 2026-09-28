def generate_document(document_type, parties, terms, dates):
    return f"""
    LEGAL DOCUMENT - {document_type}

    Parties: {parties}
    Date: {dates}
    Terms: {terms}

    This is a system generated document by LegalEase AI.
    """