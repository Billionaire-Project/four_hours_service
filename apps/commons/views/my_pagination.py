from drf_yasg import openapi


class MyPagination:
    def __init__(self, start, offset):
        self.start = start
        self.offset = offset
        self.get_params = [
            openapi.Parameter(
                "start",
                openapi.IN_QUERY,
                description="시작",
                type=openapi.TYPE_INTEGER,
                default=start,
            ),
            openapi.Parameter(
                "offset",
                openapi.IN_QUERY,
                description="개수",
                type=openapi.TYPE_INTEGER,
                default=offset,
            ),
        ]

    def get(self, request, queryset):
        start = int(request.query_params.get("start") or self.start)
        offset = int(request.query_params.get("offset") or self.offset)
        end = start + offset

        while True:
            print(f"\n\n\nend: {end}\n\n\n")
            if queryset[end - 1 : end].exists():
                if (
                    queryset[end - 1 : end][0].created_at.date()
                    == queryset[end : end + 1][0].created_at.date()
                ):
                    end += 1
                    continue
                else:
                    _next = str(end)
                    break
            else:
                _next = None
                break

        result = queryset[start:end]

        resp = {
            "start": str(start),
            "offset": str(offset),
            "next": _next,
            "result": result,
        }

        return resp
