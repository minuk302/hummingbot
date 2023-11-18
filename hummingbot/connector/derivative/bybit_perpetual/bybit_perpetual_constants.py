from hummingbot.core.data_type.common import OrderType, PositionMode
from hummingbot.core.data_type.in_flight_order import OrderState

EXCHANGE_NAME = "bybit_perpetual"

DEFAULT_DOMAIN = "bybit_perpetual_main"

DEFAULT_TIME_IN_FORCE = "GoodTillCancel"

REST_URLS = {"bybit_perpetual_main": "https://api.bybit.com/",
             "bybit_perpetual_testnet": "https://api-testnet.bybit.com/"}
WSS_NON_LINEAR_PUBLIC_URLS = {"bybit_perpetual_main": "wss://stream.bybit.com/v5/public/linear",
                              "bybit_perpetual_testnet": "wss://stream-testnet.bybit.com/v5/public/linear"}
WSS_NON_LINEAR_PRIVATE_URLS = {"bybit_perpetual_main": "wss://stream.bybit.com/v5/private",
                               "bybit_perpetual_testnet": "wss://stream-testnet.bybit.com/v5/private"}
WSS_LINEAR_PUBLIC_URLS = WSS_NON_LINEAR_PUBLIC_URLS
WSS_LINEAR_PRIVATE_URLS = WSS_NON_LINEAR_PRIVATE_URLS

REST_API_VERSION = "v5"

HBOT_BROKER_ID = "Hummingbot"

MAX_ID_LEN = 36
SECONDS_TO_WAIT_TO_RECEIVE_MESSAGE = 30
POSITION_IDX_ONEWAY = 0
POSITION_IDX_HEDGE_BUY = 1
POSITION_IDX_HEDGE_SELL = 2

ORDER_TYPE_MAP = {
    OrderType.LIMIT: "Limit",
    OrderType.MARKET: "Market",
}

POSITION_MODE_API_ONEWAY = 0
POSITION_MODE_API_HEDGE = 3
POSITION_MODE_MAP = {
    PositionMode.ONEWAY: POSITION_MODE_API_ONEWAY,
    PositionMode.HEDGE: POSITION_MODE_API_HEDGE,
}

# REST API Public Endpoints
LINEAR_MARKET = "linear"
NON_LINEAR_MARKET = "non_linear"

LATEST_SYMBOL_INFORMATION_ENDPOINT = {
    LINEAR_MARKET: f"{REST_API_VERSION}/market/tickers",
    NON_LINEAR_MARKET: f"{REST_API_VERSION}/market/tickers"}
QUERY_SYMBOL_ENDPOINT = {
    LINEAR_MARKET: f"{REST_API_VERSION}/market/instruments-info",
    NON_LINEAR_MARKET: f"{REST_API_VERSION}/market/instruments-info"}
ORDER_BOOK_ENDPOINT = {
    LINEAR_MARKET: f"{REST_API_VERSION}/market/orderbook",
    NON_LINEAR_MARKET: f"{REST_API_VERSION}/market/orderbook"}
SERVER_TIME_PATH_URL = {
    LINEAR_MARKET: f"{REST_API_VERSION}/market/time",
    NON_LINEAR_MARKET: f"{REST_API_VERSION}/market/time"
}

# REST API Private Endpoints
SET_LEVERAGE_PATH_URL = {
    LINEAR_MARKET: f"{REST_API_VERSION}/position/set-leverage",
    NON_LINEAR_MARKET: f"{REST_API_VERSION}/position/set-leverage"}
GET_LAST_FUNDING_RATE_PATH_URL = {
    LINEAR_MARKET: f"{REST_API_VERSION}/market/funding/history",
    NON_LINEAR_MARKET: f"{REST_API_VERSION}/market/funding/history"}
GET_PREDICTED_FUNDING_RATE_PATH_URL = {
    LINEAR_MARKET: "/private/linear/funding/predicted-funding",
    NON_LINEAR_MARKET: f"{REST_API_VERSION}/private/funding/predicted-funding"
}
GET_POSITIONS_PATH_URL = {
    LINEAR_MARKET: f"{REST_API_VERSION}/position/list",
    NON_LINEAR_MARKET: f"{REST_API_VERSION}/position/list"}
PLACE_ACTIVE_ORDER_PATH_URL = {
    LINEAR_MARKET: f"{REST_API_VERSION}/order/create",
    NON_LINEAR_MARKET: f"{REST_API_VERSION}/order/create"}
CANCEL_ACTIVE_ORDER_PATH_URL = {
    LINEAR_MARKET: f"{REST_API_VERSION}/order/cancel",
    NON_LINEAR_MARKET: f"{REST_API_VERSION}/order/cancel"}
CANCEL_ALL_ACTIVE_ORDERS_PATH_URL = {
    LINEAR_MARKET: f"{REST_API_VERSION}/order/cancel-all",
    NON_LINEAR_MARKET: f"{REST_API_VERSION}/order/cancel-all"}
QUERY_ACTIVE_ORDER_PATH_URL = {
    LINEAR_MARKET: f"{REST_API_VERSION}/order/realtime",
    NON_LINEAR_MARKET: f"{REST_API_VERSION}/order/realtime"}
USER_TRADE_RECORDS_PATH_URL = {
    LINEAR_MARKET: f"{REST_API_VERSION}/execution/list",
    NON_LINEAR_MARKET: f"{REST_API_VERSION}/execution/list"}
GET_WALLET_BALANCE_PATH_URL = {
    LINEAR_MARKET: f"{REST_API_VERSION}/account/wallet-balance",
    NON_LINEAR_MARKET: f"{REST_API_VERSION}/account/wallet-balance"}
SET_POSITION_MODE_URL = {
    LINEAR_MARKET: f"{REST_API_VERSION}/position/switch-mode"}

# Funding Settlement Time Span
FUNDING_SETTLEMENT_DURATION = (5, 5)  # seconds before snapshot, seconds after snapshot

# WebSocket Public Endpoints
WS_PING_REQUEST = "ping"
WS_ORDER_BOOK_EVENTS_TOPIC = "orderbook.200"
WS_TRADES_TOPIC = "trade"
WS_INSTRUMENTS_INFO_TOPIC = "instrument_info.100ms"
WS_AUTHENTICATE_USER_ENDPOINT_NAME = "auth"
WS_SUBSCRIPTION_POSITIONS_ENDPOINT_NAME = "position"
WS_SUBSCRIPTION_ORDERS_ENDPOINT_NAME = "order"
WS_SUBSCRIPTION_EXECUTIONS_ENDPOINT_NAME = "execution"
WS_SUBSCRIPTION_WALLET_ENDPOINT_NAME = "wallet"

# Order Statuses
ORDER_STATE = {
    "Created": OrderState.OPEN,
    "New": OrderState.OPEN,
    "Filled": OrderState.FILLED,
    "PartiallyFilled": OrderState.PARTIALLY_FILLED,
    "Cancelled": OrderState.CANCELED,
    "PendingCancel": OrderState.PENDING_CANCEL,
    "Rejected": OrderState.FAILED,
}

GET_LIMIT_ID = "GETLimit"
POST_LIMIT_ID = "POSTLimit"
GET_RATE = 49  # per second
POST_RATE = 19  # per second

NON_LINEAR_PRIVATE_BUCKET_100_LIMIT_ID = "NonLinearPrivateBucket100"
NON_LINEAR_PRIVATE_BUCKET_600_LIMIT_ID = "NonLinearPrivateBucket600"
NON_LINEAR_PRIVATE_BUCKET_75_LIMIT_ID = "NonLinearPrivateBucket75"
NON_LINEAR_PRIVATE_BUCKET_120_B_LIMIT_ID = "NonLinearPrivateBucket120B"
NON_LINEAR_PRIVATE_BUCKET_120_C_LIMIT_ID = "NonLinearPrivateBucket120C"

LINEAR_PRIVATE_BUCKET_100_LIMIT_ID = "LinearPrivateBucket100"
LINEAR_PRIVATE_BUCKET_600_LIMIT_ID = "LinearPrivateBucket600"
LINEAR_PRIVATE_BUCKET_75_LIMIT_ID = "LinearPrivateBucket75"
LINEAR_PRIVATE_BUCKET_120_A_LIMIT_ID = "LinearPrivateBucket120A"

# Request error codes
RET_CODE_OK = 0
RET_CODE_PARAMS_ERROR = 10001
RET_CODE_API_KEY_INVALID = 10003
RET_CODE_AUTH_TIMESTAMP_ERROR = 10021
RET_CODE_ORDER_NOT_EXISTS = 20001
RET_CODE_MODE_POSITION_NOT_EMPTY = 30082
RET_CODE_MODE_NOT_MODIFIED = 110025
RET_CODE_MODE_ORDER_NOT_EMPTY = 30086
RET_CODE_API_KEY_EXPIRED = 33004
RET_CODE_LEVERAGE_NOT_MODIFIED = 34036
RET_CODE_POSITION_ZERO = 130125
