def format_linter_error(error: dict) -> dict:
    return {"line": error["line_number"], "column": error["column_number"],
            "message": error["text"], "name": error["code"],
            "source": "flake8"} if len(error) > 0 else {}
    pass


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {"errors":
            [{"line": error["line_number"],
              "column": error["column_number"],
              "message": error["text"], "name": error["code"],
              "source": "flake8"}
             if len(error) > 0 else {} for error in errors],
            "path": file_path, "status": "failed"
            if len(errors) > 0 else "passed"}
    pass


def format_linter_report(linter_report: dict) -> list:
    return [{"errors":
            [{"line": error["line_number"], "column": error["column_number"],
              "message": error["text"], "name": error["code"],
              "source": "flake8"}
             if len(error) > 0 else {} for error in errors],
            "path": name, "status": "failed" if len(errors) > 0 else "passed"}
            for name, errors in linter_report.items()]
    pass
