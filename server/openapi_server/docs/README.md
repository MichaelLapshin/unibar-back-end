# Documentation for UniBar API

<a name="documentation-for-api-endpoints"></a>
## Documentation for API Endpoints

All URIs are relative to *http://localhost*

| Class | Method | HTTP request | Description |
|------------ | ------------- | ------------- | -------------|
| *DefaultApi* | [**adminMessagesListGet**](Apis/DefaultApi.md#adminmessageslistget) | **GET** /admin/messages/list |  |
*DefaultApi* | [**adminOrdersListGet**](Apis/DefaultApi.md#adminorderslistget) | **GET** /admin/orders/list |  |
*DefaultApi* | [**adminReportsListGet**](Apis/DefaultApi.md#adminreportslistget) | **GET** /admin/reports/list |  |
*DefaultApi* | [**adminUserUserIdGet**](Apis/DefaultApi.md#adminuseruseridget) | **GET** /admin/user/{user_id} |  |
*DefaultApi* | [**adminUsersListGet**](Apis/DefaultApi.md#adminuserslistget) | **GET** /admin/users/list |  |
*DefaultApi* | [**messageGet**](Apis/DefaultApi.md#messageget) | **GET** /message |  |
*DefaultApi* | [**ordersAvailableGet**](Apis/DefaultApi.md#ordersavailableget) | **GET** /orders/available |  |
*DefaultApi* | [**ordersOrderIdGet**](Apis/DefaultApi.md#ordersorderidget) | **GET** /orders/{order_id} |  |
*DefaultApi* | [**pingGet**](Apis/DefaultApi.md#pingget) | **GET** /ping |  |
*DefaultApi* | [**userUserIdInfoGet**](Apis/DefaultApi.md#useruseridinfoget) | **GET** /user/{user_id}/info |  |
*DefaultApi* | [**userUserIdOrderCompletePut**](Apis/DefaultApi.md#useruseridordercompleteput) | **PUT** /user/{user_id}/order/complete |  |
*DefaultApi* | [**userUserIdOrderDeliverPut**](Apis/DefaultApi.md#useruseridorderdeliverput) | **PUT** /user/{user_id}/order/deliver |  |
*DefaultApi* | [**userUserIdOrderReportPut**](Apis/DefaultApi.md#useruseridorderreportput) | **PUT** /user/{user_id}/order/report |  |
*DefaultApi* | [**userUserIdOrderRequestPut**](Apis/DefaultApi.md#useruseridorderrequestput) | **PUT** /user/{user_id}/order/request |  |
*DefaultApi* | [**userUserIdOrdersDeliveringGet**](Apis/DefaultApi.md#useruseridordersdeliveringget) | **GET** /user/{user_id}/orders/delivering |  |
*DefaultApi* | [**userUserIdOrdersRequestingGet**](Apis/DefaultApi.md#useruseridordersrequestingget) | **GET** /user/{user_id}/orders/requesting |  |
*DefaultApi* | [**usersLoginGet**](Apis/DefaultApi.md#usersloginget) | **GET** /users/login | Log in a user. |
*DefaultApi* | [**usersRegisterPost**](Apis/DefaultApi.md#usersregisterpost) | **POST** /users/register | Create a new user. |


<a name="documentation-for-models"></a>
## Documentation for Models

 - [Message](./Models/Message.md)
 - [Order](./Models/Order.md)
 - [Report](./Models/Report.md)
 - [User](./Models/User.md)


<a name="documentation-for-authorization"></a>
## Documentation for Authorization

<a name="UserAuth"></a>
### UserAuth

- **Type**: HTTP basic authentication

<a name="UserToken"></a>
### UserToken

- **Type**: API key
- **API key parameter name**: user_token
- **Location**: 

<a name="AdminToken"></a>
### AdminToken

- **Type**: API key
- **API key parameter name**: admin_token
- **Location**: HTTP header

