import asyncio
import json
import traceback
from datetime import datetime
from fastapi.responses import ORJSONResponse
import httpx
from fastapi import APIRouter, Depends
from dateutil.relativedelta import relativedelta
from api.params import RequestParam, PerformanceRequestParam, CustomerPerformanceRequestParam, DealRequestParam
from config import appConfig

router = APIRouter()

@router.get("/api/v1/review", response_class=ORJSONResponse)
async def async_get(request_params: RequestParam = Depends(RequestParam)):
    params = set_default_dates(request_params)
    '''cache_key = 'TEST_ACCOUNT'
    cache_field = f'review_performance_benchmark_{json.dumps(params)}'
    cached_data = await get_data_from_cache(cache_key, cache_field)

    if cached_data and cached_data != '{}':
        return json.loads(cached_data)'''
    async with httpx.AsyncClient(verify=False) as client:
        for key, value in dict(params).items():
            if value is None:
                del params[key]
        timeout = None
        if params.get('sub_type') == 'distributor' or params.get('user_type') == 'distributor':
            results = await asyncio.gather(
                client.get(appConfig.TOP_SUMMARY_URL, params=params, timeout=timeout),
                client.get(appConfig.CUSTOMER_SEGMENT_URL, params=params, timeout=timeout),
                client.get(appConfig.PERFORMANCE_VALUES_URL, params=params, timeout=timeout),
                client.get(appConfig.PERFORMANCE_OVER_TIME_URL, params=params, timeout=timeout),
                client.get(appConfig.PEER_PERFORMANCE_URL, params=params, timeout=timeout),
                client.get(appConfig.NUMBER_OF_OPPS_URL, params=params, timeout=timeout),
                client.get(appConfig.PERFORMANCE_DATA_URL, params=params, timeout=timeout),
                client.get(appConfig.OPP_AMOUNT_URL, params=params, timeout=timeout),
                client.get(appConfig.GROSS_REVENUE_RETENTION_URL, params=params, timeout=timeout),
                client.get(appConfig.DATE_UPDATED_URL, params=params, timeout=timeout),
                return_exceptions=True
            )
        else:
            results = await asyncio.gather(
                client.get(appConfig.TOTAL_AND_ANNUALIZED_OPP_AMOUNT_URL, params=params, timeout=timeout),
                client.get(appConfig.OPPORTUNITIES_BOOKED_URL, params=params, timeout=timeout),
                client.get(appConfig.CUSTOMER_URL, params=params, timeout=timeout),
                client.get(appConfig.CUSTOMER_SEGMENT_URL, params=params, timeout=timeout),
                client.get(appConfig.PERFORMANCE_VALUES_URL, params=params, timeout=timeout),
                client.get(appConfig.PERFORMANCE_OVER_TIME_URL, params=params, timeout=timeout),
                client.get(appConfig.PEER_PERFORMANCE_URL, params=params, timeout=timeout),
                client.get(appConfig.NUMBER_OF_OPPS_URL, params=params, timeout=timeout),
                client.get(appConfig.PERFORMANCE_DATA_URL, params=params, timeout=timeout),
                client.get(appConfig.OPP_AMOUNT_URL, params=params, timeout=timeout),
                client.get(appConfig.GROSS_REVENUE_RETENTION_URL, params=params, timeout=timeout),
                client.get(appConfig.GET_CUSTOMER_RETENTION_URL, params=params, timeout=timeout),
                client.get(appConfig.DATE_UPDATED_URL, params=params, timeout=timeout),
                return_exceptions=True
            )

    #for s in snapshot.statistics("filename"):
     #   print(s)
    #for s in snapshot.statistics("lineno"):
     #   print(s)
    await client.aclose()

    return get_output(results)


@router.get("/api/v1/review/performance", response_class=ORJSONResponse)
async def async_get_performance(request_params: PerformanceRequestParam = Depends(PerformanceRequestParam)):
    params = set_default_dates(request_params)
    '''cache_key = 'TEST_ACCOUNT'
    cache_field = f'review_performance_benchmark_{json.dumps(params)}'
    cached_data = await get_data_from_cache(cache_key, cache_field)
    if cached_data and cached_data != '{}':
        return json.loads(cached_data)'''
    results = None
    async with httpx.AsyncClient() as client:
        for key, value in dict(params).items():
            if value is None:
                del params[key]
        timeout = httpx.Timeout(timeout=30)
        if params.get('sub_type') == 'distributor' or params.get('user_type') == 'distributor':
            results = await asyncio.gather(
                client.get(appConfig.TOP_SUMMARY_URL, params=params, timeout=timeout),
                client.get(appConfig.CUSTOMER_RETENTION_CHART_URL, params=params, timeout=timeout),
                client.get(appConfig.GET_BOOKINGS_PERFORMANCE_AMOUNT, params=params, timeout=timeout),
                client.get(appConfig.GROSS_REVENUE_RETENTION_URL, params=params, timeout=timeout),
                client.get(appConfig.NET_REVENUE_RETENTION_URL, params=params, timeout=timeout),
                client.get(appConfig.GET_CUSTOMER_RETENTION_URL, params=params, timeout=timeout),
                client.get(appConfig.GET_OPPORTUNITY_DETAILS_TABLE_URL, params=params, timeout=timeout),
                client.get(appConfig.GET_DETAILS_BY_CUSTOMER_TABLE_URL, params=params, timeout=timeout),
                client.get(appConfig.CUSTOMER_SEGMENT_URL, params=params, timeout=timeout),
                client.get(appConfig.DATE_UPDATED_URL, params=params, timeout=timeout),
                return_exceptions=True
            )
        else:
            results = await asyncio.gather(
                client.get(appConfig.TOTAL_AND_ANNUALIZED_OPP_AMOUNT_URL, params=params, timeout=timeout),
                client.get(appConfig.OPPORTUNITIES_BOOKED_URL, params=params, timeout=timeout),
                client.get(appConfig.CUSTOMER_URL, params=params, timeout=timeout),
                client.get(appConfig.CUSTOMER_RETENTION_CHART_URL, params=params, timeout=timeout),
                client.get(appConfig.GET_BOOKINGS_PERFORMANCE_AMOUNT, params=params, timeout=timeout),
                client.get(appConfig.GROSS_REVENUE_RETENTION_URL, params=params, timeout=timeout),
                client.get(appConfig.NET_REVENUE_RETENTION_URL, params=params, timeout=timeout),
                client.get(appConfig.GET_CUSTOMER_RETENTION_URL, params=params, timeout=timeout),
                client.get(appConfig.GET_OPPORTUNITY_DETAILS_TABLE_URL, params=params, timeout=timeout),
                client.get(appConfig.GET_DETAILS_BY_CUSTOMER_TABLE_URL, params=params, timeout=timeout),
                client.get(appConfig.CUSTOMER_SEGMENT_URL, params=params, timeout=timeout),
                client.get(appConfig.DATE_UPDATED_URL, params=params, timeout=timeout),
                return_exceptions=True
            )

    # return get_output(results)
    out = {}
    for r in results:
        if isinstance(r, Exception):
            print(f'Exception occurred...{r.request}')
            print(''.join(traceback.format_exception(etype=type(r), value=r, tb=r.__traceback__)))
        elif r.status_code != 200:
            print(f'Request failed.{r.request}')
        else:
            print(r)
            print(r.status_code)
            d = dict(r.json())
            for key, value in d.items():
                if key in out and type(value) is dict:
                    if key == 'deal_management':
                        for k, v in value.items():
                            if k in out[key] and type(out[key][k]) is dict:
                                out[key][k].update(v)
                            elif type(out[key]) is dict:
                                out[key].update(value)
                    else:
                        out[key].update(value)
                else:
                    out.update(d)


    return out
    '''print(f'cache_key: {cache_key}')
    print(f'cache_field: {cache_field}')
    background_tasks.add_task(parse_data_to_cache, key=cache_key, field=cache_field, data=json.dumps(out))'''


@router.get("/api/v1/review/deal-management", response_class=ORJSONResponse)
async def async_get(request_params: RequestParam = Depends(DealRequestParam)
):
    params = set_default_dates(request_params)
    async with httpx.AsyncClient() as client:
        for key, value in dict(params).items():
            if value is None:
                del params[key]
        timeout = httpx.Timeout(timeout=30)
        if params.get('sub_type') == 'distributor' or params.get('user_type') == 'distributor':
            results = await asyncio.gather(
                client.get(appConfig.TOP_SUMMARY_URL, params=params, timeout=timeout),
                client.get(appConfig.DEAL_MANAGEMENT_TRANSFERRED_IN_URL, params=params, timeout=timeout),
                client.get(appConfig.DEAL_MANAGEMENT_TRANSFERRED_OUT_URL, params=params, timeout=timeout),
                client.get(appConfig.DEAL_MANAGEMENT_CLOSED_LOST_URL, params=params, timeout=timeout),
                client.get(appConfig.DEAL_MANAGEMENT_OPPORTUNITY_DETAILS_TABLE_URL, params=params, timeout=timeout),
                client.get(appConfig.NET_REVENUE_RETENTION_URL, params=params, timeout=timeout),
                client.get(appConfig.OPP_AMOUNT_URL, params=params, timeout=timeout),
                client.get(appConfig.DATE_UPDATED_URL, params=params, timeout=timeout),
                return_exceptions=True
            )
        else:
            results = await asyncio.gather(
                client.get(appConfig.TOTAL_AND_ANNUALIZED_OPP_AMOUNT_URL, params=params, timeout=timeout),
                client.get(appConfig.OPPORTUNITIES_BOOKED_URL, params=params, timeout=timeout),
                client.get(appConfig.CUSTOMER_URL, params=params, timeout=timeout),
                client.get(appConfig.DEAL_MANAGEMENT_TRANSFERRED_IN_URL, params=params, timeout=timeout),
                client.get(appConfig.DEAL_MANAGEMENT_TRANSFERRED_OUT_URL, params=params, timeout=timeout),
                client.get(appConfig.DEAL_MANAGEMENT_CLOSED_LOST_URL, params=params, timeout=timeout),
                client.get(appConfig.DEAL_MANAGEMENT_OPPORTUNITY_DETAILS_TABLE_URL, params=params, timeout=timeout),
                client.get(appConfig.NET_REVENUE_RETENTION_URL, params=params, timeout=timeout),
                client.get(appConfig.OPP_AMOUNT_URL, params=params, timeout=timeout),
                client.get(appConfig.DATE_UPDATED_URL, params=params, timeout=timeout),
                return_exceptions=True
            )

    return get_output(results)


@router.get("/api/v1/review/customer-performance", response_class=ORJSONResponse)
async def customer_performance(request_params: CustomerPerformanceRequestParam = Depends(CustomerPerformanceRequestParam),
):
    params = set_default_dates(request_params)
    async with httpx.AsyncClient() as client:
        for key, value in dict(params).items():
            if value is None:
                del params[key]
        timeout = httpx.Timeout(timeout=30)
        if params.get('sub_type') == 'distributor' or params.get('user_type') == 'distributor':
            results = await asyncio.gather(
                client.get(appConfig.TOP_SUMMARY_URL, params=params, timeout=timeout),
                client.get(appConfig.PERFORMANCE_CHART_DATA_URL, params=params, timeout=timeout),
                return_exceptions=True
            )
        else:
            results = await asyncio.gather(
                client.get(appConfig.TOTAL_AND_ANNUALIZED_OPP_AMOUNT_URL, params=params, timeout=timeout),
                client.get(appConfig.OPPORTUNITIES_BOOKED_URL, params=params, timeout=timeout),
                client.get(appConfig.CUSTOMER_URL, params=params, timeout=timeout),
                client.get(appConfig.PERFORMANCE_CHART_DATA_URL, params=params, timeout=timeout),
                return_exceptions=True
            )
    return get_output(results)


@router.get("/api/v1/date-updated")
async def get_updated_date():
    return {'updated': datetime.now().astimezone().strftime("%B %d, %Y %I:%M %p %Z")}


def set_default_dates(request_params):
    now = datetime.now()
    end_date = now + relativedelta(months=-1)
    start_date = end_date + relativedelta(months=-11)
    data = json.loads(request_params.json())
    data.update({
        'start_month': request_params.start_month or f'{start_date.month}',
        'start_year': request_params.start_year or f'{start_date.year}',
        'end_month': request_params.end_month or f'{end_date.month}',
        'end_year': request_params.end_year or f'{end_date.year}',
    })
    return data


def get_output(results):
    out = {}
    for r in results:
        if isinstance(r, Exception):
            print(f'Exception occurred...{r.request}')
            print(''.join(traceback.format_exception(etype=type(r), value=r, tb=r.__traceback__)))
        elif r.status_code != 200:
            print(f'Request failed.{r.request}')
        else:
           # print(r)
           # print(r.status_code)
            d = dict(r.json())
            for key, value in d.items():
                if key in out and type(value) is dict:
                    if key == 'deal_management':
                        for k, v in value.items():
                            if k in out[key] and type(out[key][k]) is dict:
                                out[key][k].update(v)
                            elif type(out[key]) is dict:
                                out[key].update(value)
                    else:
                        out[key].update(value)
                else:
                    out.update(d)

    return out
