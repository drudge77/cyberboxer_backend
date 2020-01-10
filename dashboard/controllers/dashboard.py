from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from dashboard.models.cs_score import CSScore
from dashboard.models.netd_score import NetdScore
from dashboard.models.ponemon_score import PonemonScore
from cyberboxer_backend.utils import response_format


class DashboardAPIView(APIView):

    def get(self, request):
        naics_code = request.GET.get('naics_code', None)
        band = request.GET.get('band', None)
        cs_score, severity, ps, netd_score, ponemon_score = None, None, None, None, None
        cs_obj = CSScore.objects.filter(naics_code=naics_code, band=band).first()
        if cs_obj:
            cs_score = cs_obj.score
            if cs_obj.frequency and cs_obj.severity:
                ps = {'severity': cs_obj.severity, 'frequency': cs_obj.frequency}

        netd_obj = NetdScore.objects.filter(naics_code=naics_code).first()
        if netd_obj:
            netd_score = netd_obj.netd_score

        ponemon_obj = PonemonScore.objects.filter(naics_code=naics_code).first()
        if ponemon_obj:
            ponemon_score = ponemon_obj.ponemon_score

        context = {
            'cs_score': cs_score,
            'ps': ps,
            'netd_score': netd_score,
            'ponemon_score': ponemon_score
        }

        msg = "Dashboard API data"
        context = response_format(success=False, message=msg, data=context)
        return Response(context, status=status.HTTP_201_CREATED)
