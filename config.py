# config.py
import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    PORT = os.getenv('PORT')
    DATA_SERVICE_HOST = os.getenv('DATA_SERVICE_HOST')
    DATA_SERVICE_PORT = os.getenv('DATA_SERVICE_PORT')
    TOTAL_AND_ANNUALIZED_OPP_AMOUNT_URL = f"{DATA_SERVICE_HOST}/api/v1/review/total-opp-amount"
    TOP_SUMMARY_URL = f"{DATA_SERVICE_HOST}/api/v1/review/top-summary"
    PERFORMANCE_DATA_URL = f"{DATA_SERVICE_HOST}/api/v1/review/performance-data"
    DATE_UPDATED_URL = f"{DATA_SERVICE_HOST}/api/v1/date-updated"
    PERFORMANCE_CHART_DATA_URL = f"{DATA_SERVICE_HOST}/api/v1/review/performance-chart-data"
    OPPORTUNITIES_BOOKED_URL = f"{DATA_SERVICE_HOST}/api/v1/review/booked-opps"
    CUSTOMER_URL = f"{DATA_SERVICE_HOST}/api/v1/review/customers"
    CUSTOMER_SEGMENT_URL = f"{DATA_SERVICE_HOST}/api/v1/review/customer-segment"
    PERFORMANCE_VALUES_URL = f"{DATA_SERVICE_HOST}/api/v1/review/performance-values"
    PERFORMANCE_OVER_TIME_URL = f"{DATA_SERVICE_HOST}/api/v1/review/performance-over-time"
    PEER_PERFORMANCE_URL = f"{DATA_SERVICE_HOST}/api/v1/review/peer-performance"
    NUMBER_OF_OPPS_URL = f"{DATA_SERVICE_HOST}/api/v1/review/number-of-opps"
    OPPS_BY_CUSTOMER_URL = f"{DATA_SERVICE_HOST}/api/v1/review/customer-performance"
    OPP_AMOUNT_URL = f"{DATA_SERVICE_HOST}/api/v1/review/opp-amount"
    GROSS_REVENUE_RETENTION_URL = f"{DATA_SERVICE_HOST}/api/v1/review/gross-rev"
    GET_CUSTOMER_RETENTION_URL = f"{DATA_SERVICE_HOST}/api/v1/review/customer-retention-rate"
    GET_OPPORTUNITY_DETAILS_TABLE_URL = f"{DATA_SERVICE_HOST}/api/v1/review/opp-details-table"
    NET_REVENUE_RETENTION_URL = f"{DATA_SERVICE_HOST}/api/v1/review/net-rev"
    CUSTOMER_RETENTION_CHART_URL = f"{DATA_SERVICE_HOST}/api/v1/review/customer-retention-chart"
    GET_BOOKINGS_PERFORMANCE_AMOUNT = f"{DATA_SERVICE_HOST}/api/v1/review/bookings-performance-amount"
    GET_DETAILS_BY_CUSTOMER_TABLE_URL = f"{DATA_SERVICE_HOST}/api/v1/review/details-by-customer"
    DEAL_MANAGEMENT_TRANSFERRED_IN_URL = f"{DATA_SERVICE_HOST}/api/v1/review/transferred-in"
    DEAL_MANAGEMENT_TRANSFERRED_OUT_URL = f"{DATA_SERVICE_HOST}/api/v1/review/transferred-out"
    DEAL_MANAGEMENT_OPPORTUNITY_DETAILS_TABLE_URL = f"{DATA_SERVICE_HOST}/api/v1/review/deal-management-opp-details"
    DEAL_MANAGEMENT_CLOSED_LOST_URL = f"{DATA_SERVICE_HOST}/api/v1/review/closed-lost"
    CUSTOMER_PERFORMANCE_CHART_DATA_URL = f"{DATA_SERVICE_HOST}/api/v1/review/customer-performance-data"


appConfig = Config()
