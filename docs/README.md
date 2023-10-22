# Documentation for UniBar API

<a name="documentation-for-api-endpoints"></a>
## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**adminLoginPost**](Apis/DefaultApi.md#adminloginpost) | **POST** /admin/login | 
*DefaultApi* | [**adminMessagesListGet**](Apis/DefaultApi.md#adminmessageslistget) | **GET** /admin/messages/list | 
*DefaultApi* | [**adminOrdersListGet**](Apis/DefaultApi.md#adminorderslistget) | **GET** /admin/orders/list | 
*DefaultApi* | [**adminReportsListGet**](Apis/DefaultApi.md#adminreportslistget) | **GET** /admin/reports/list | 
*DefaultApi* | [**adminUsersListGet**](Apis/DefaultApi.md#adminuserslistget) | **GET** /admin/users/list | 
*DefaultApi* | [**deploymentGet**](Apis/DefaultApi.md#deploymentget) | **GET** /deployment | 
*DefaultApi* | [**messagePost**](Apis/DefaultApi.md#messagepost) | **POST** /message | 
*DefaultApi* | [**orderCancelPut**](Apis/DefaultApi.md#ordercancelput) | **PUT** /order/cancel | 
*DefaultApi* | [**orderClaimPut**](Apis/DefaultApi.md#orderclaimput) | **PUT** /order/claim | 
*DefaultApi* | [**orderCompletePut**](Apis/DefaultApi.md#ordercompleteput) | **PUT** /order/complete | 
*DefaultApi* | [**orderCreatePost**](Apis/DefaultApi.md#ordercreatepost) | **POST** /order/create | 
*DefaultApi* | [**orderOrderIdGet**](Apis/DefaultApi.md#orderorderidget) | **GET** /order/{order_id} | 
*DefaultApi* | [**orderReportPost**](Apis/DefaultApi.md#orderreportpost) | **POST** /order/report | 
*DefaultApi* | [**orderUnclaimPut**](Apis/DefaultApi.md#orderunclaimput) | **PUT** /order/unclaim | 
*DefaultApi* | [**ordersAvailableGet**](Apis/DefaultApi.md#ordersavailableget) | **GET** /orders/available | 
*DefaultApi* | [**pingGet**](Apis/DefaultApi.md#pingget) | **GET** /ping | 
*DefaultApi* | [**shutdownGet**](Apis/DefaultApi.md#shutdownget) | **GET** /shutdown | 
*DefaultApi* | [**userUserIdGet**](Apis/DefaultApi.md#useruseridget) | **GET** /user/{user_id} | 
*DefaultApi* | [**userUserIdOrdersActiveGet**](Apis/DefaultApi.md#useruseridordersactiveget) | **GET** /user/{user_id}/orders/active | 
*DefaultApi* | [**userUserIdOrdersClaimedGet**](Apis/DefaultApi.md#useruseridordersclaimedget) | **GET** /user/{user_id}/orders/claimed | 
*DefaultApi* | [**userUserIdUpdatePatch**](Apis/DefaultApi.md#useruseridupdatepatch) | **PATCH** /user/{user_id}/update | 
*DefaultApi* | [**usersLoginPost**](Apis/DefaultApi.md#usersloginpost) | **POST** /users/login | Log in a user. Set cookie auth token.
*DefaultApi* | [**usersRegisterPost**](Apis/DefaultApi.md#usersregisterpost) | **POST** /users/register | Create a new user.


<a name="documentation-for-models"></a>
## Documentation for Models

 - [BodyAdminLogin](.//Models/BodyAdminLogin.md)
 - [BodyMessage](.//Models/BodyMessage.md)
 - [BodyOrderCancel](.//Models/BodyOrderCancel.md)
 - [BodyOrderClaim](.//Models/BodyOrderClaim.md)
 - [BodyOrderComplete](.//Models/BodyOrderComplete.md)
 - [BodyOrderReport](.//Models/BodyOrderReport.md)
 - [BodyOrderRequest](.//Models/BodyOrderRequest.md)
 - [BodyOrderUnclaim](.//Models/BodyOrderUnclaim.md)
 - [BodyUserUpdate](.//Models/BodyUserUpdate.md)
 - [BodyUsersLogin](.//Models/BodyUsersLogin.md)
 - [BodyUsersRegister](.//Models/BodyUsersRegister.md)
 - [Message](.//Models/Message.md)
 - [Order](.//Models/Order.md)
 - [PaymentMethod](.//Models/PaymentMethod.md)
 - [Report](.//Models/Report.md)
 - [User](.//Models/User.md)


<a name="documentation-for-authorization"></a>
## Documentation for Authorization

<a name="AdminAuth"></a>
### AdminAuth

- **Type**: API key
- **API key parameter name**: admin_token
- **Location**: 

<a name="UserAuth"></a>
### UserAuth

- **Type**: API key
- **API key parameter name**: user_token
- **Location**: 

