from drf_yasg import openapi


class Pagination:
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

    def get(self, request, model):
        queryset = model.objects.all().order_by("-created_at")
        start = int(request.query_params.get("start") or self.start)
        offset = int(request.query_params.get("offset") or self.offset)
        result = queryset[start : start + offset]

        if len(result) < 0:
            return None

        return result
