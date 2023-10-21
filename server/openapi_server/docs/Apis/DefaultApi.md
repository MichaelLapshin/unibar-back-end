# DefaultApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**adminMessagesListGet**](DefaultApi.md#adminMessagesListGet) | **GET** /admin/messages/list |  |
| [**adminOrdersListGet**](DefaultApi.md#adminOrdersListGet) | **GET** /admin/orders/list |  |
| [**adminReportsListGet**](DefaultApi.md#adminReportsListGet) | **GET** /admin/reports/list |  |
| [**adminUserUserIdGet**](DefaultApi.md#adminUserUserIdGet) | **GET** /admin/user/{user_id} |  |
| [**adminUsersListGet**](DefaultApi.md#adminUsersListGet) | **GET** /admin/users/list |  |
| [**messageGet**](DefaultApi.md#messageGet) | **GET** /message |  |
| [**ordersAvailableGet**](DefaultApi.md#ordersAvailableGet) | **GET** /orders/available |  |
| [**ordersOrderIdGet**](DefaultApi.md#ordersOrderIdGet) | **GET** /orders/{order_id} |  |
| [**pingGet**](DefaultApi.md#pingGet) | **GET** /ping |  |
| [**userUserIdInfoGet**](DefaultApi.md#userUserIdInfoGet) | **GET** /user/{user_id}/info |  |
| [**userUserIdOrderCompletePut**](DefaultApi.md#userUserIdOrderCompletePut) | **PUT** /user/{user_id}/order/complete |  |
| [**userUserIdOrderDeliverPut**](DefaultApi.md#userUserIdOrderDeliverPut) | **PUT** /user/{user_id}/order/deliver |  |
| [**userUserIdOrderReportPut**](DefaultApi.md#userUserIdOrderReportPut) | **PUT** /user/{user_id}/order/report |  |
| [**userUserIdOrderRequestPut**](DefaultApi.md#userUserIdOrderRequestPut) | **PUT** /user/{user_id}/order/request |  |
| [**userUserIdOrdersDeliveringGet**](DefaultApi.md#userUserIdOrdersDeliveringGet) | **GET** /user/{user_id}/orders/delivering |  |
| [**userUserIdOrdersRequestingGet**](DefaultApi.md#userUserIdOrdersRequestingGet) | **GET** /user/{user_id}/orders/requesting |  |
| [**usersLoginGet**](DefaultApi.md#usersLoginGet) | **GET** /users/login | Log in a user. |
| [**usersRegisterPost**](DefaultApi.md#usersRegisterPost) | **POST** /users/register | Create a new user. |


<a name="adminMessagesListGet"></a>
# **adminMessagesListGet**
> List adminMessagesListGet()



### Parameters
This endpoint does not need any parameter.

### Return type

[**List**](../Models/Message.md)

### Authorization

[AdminToken](../README.md#AdminToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: user_ids

<a name="adminOrdersListGet"></a>
# **adminOrdersListGet**
> List adminOrdersListGet()



### Parameters
This endpoint does not need any parameter.

### Return type

[**List**](../Models/Order.md)

### Authorization

[AdminToken](../README.md#AdminToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: user_ids

<a name="adminReportsListGet"></a>
# **adminReportsListGet**
> List adminReportsListGet()



### Parameters
This endpoint does not need any parameter.

### Return type

[**List**](../Models/Order.md)

### Authorization

[AdminToken](../README.md#AdminToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: user_ids

<a name="adminUserUserIdGet"></a>
# **adminUserUserIdGet**
> User adminUserUserIdGet(user\_id)



### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **user\_id** | **UUID**| User of which to fetch information about. | [default to null] |

### Return type

[**User**](../Models/User.md)

### Authorization

[AdminToken](../README.md#AdminToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: user

<a name="adminUsersListGet"></a>
# **adminUsersListGet**
> List adminUsersListGet()



### Parameters
This endpoint does not need any parameter.

### Return type

[**List**](../Models/User.md)

### Authorization

[AdminToken](../README.md#AdminToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: user_ids

<a name="messageGet"></a>
# **messageGet**
> messageGet(message, user\_id, email)



### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **message** | **String**| Message to send to UniBar. | [default to null] |
| **user\_id** | **UUID**| User that wants to send a message. | [optional] [default to null] |
| **email** | **String**| Email of the person sending the message. | [optional] [default to null] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

<a name="ordersAvailableGet"></a>
# **ordersAvailableGet**
> List ordersAvailableGet()



### Parameters
This endpoint does not need any parameter.

### Return type

[**List**](../Models/Order.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: orders

<a name="ordersOrderIdGet"></a>
# **ordersOrderIdGet**
> Order ordersOrderIdGet(order\_id)



### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **order\_id** | **UUID**| Identification of the order. | [default to null] |

### Return type

[**Order**](../Models/Order.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: order

<a name="pingGet"></a>
# **pingGet**
> pingGet()



### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

<a name="userUserIdInfoGet"></a>
# **userUserIdInfoGet**
> User userUserIdInfoGet(user\_id)



### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **user\_id** | **UUID**| Identifying the user. | [default to null] |

### Return type

[**User**](../Models/User.md)

### Authorization

[AdminToken](../README.md#AdminToken), [UserToken](../README.md#UserToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: orders

<a name="userUserIdOrderCompletePut"></a>
# **userUserIdOrderCompletePut**
> userUserIdOrderCompletePut(user\_id, order\_id)



### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **user\_id** | **UUID**| User whose order is complete and is giving a delivery-token to the deliverer. | [default to null] |
| **order\_id** | **UUID**| Order that is complete and for which a delivery-token must be transfered. | [default to null] |

### Return type

null (empty response body)

### Authorization

[AdminToken](../README.md#AdminToken), [UserToken](../README.md#UserToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

<a name="userUserIdOrderDeliverPut"></a>
# **userUserIdOrderDeliverPut**
> userUserIdOrderDeliverPut(user\_id, order\_id)



### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **user\_id** | **UUID**| User to fulfil the order. | [default to null] |
| **order\_id** | **UUID**| Order to deliver. | [default to null] |

### Return type

null (empty response body)

### Authorization

[AdminToken](../README.md#AdminToken), [UserToken](../README.md#UserToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

<a name="userUserIdOrderReportPut"></a>
# **userUserIdOrderReportPut**
> userUserIdOrderReportPut(user\_id, reported\_id, order\_id, message)



### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **user\_id** | **UUID**| User that is reporting. | [default to null] |
| **reported\_id** | **UUID**| User that is reported. | [default to null] |
| **order\_id** | **UUID**| Order in which the report happened. | [default to null] |
| **message** | **UUID**| Report message from the user reporting. | [default to null] |

### Return type

null (empty response body)

### Authorization

[AdminToken](../README.md#AdminToken), [UserToken](../README.md#UserToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

<a name="userUserIdOrderRequestPut"></a>
# **userUserIdOrderRequestPut**
> userUserIdOrderRequestPut(user\_id, order)



### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **user\_id** | **UUID**| Identifying the user. | [default to null] |
| **order** | [**Order**](../Models/.md)| Delivery request order of the user. | [default to null] |

### Return type

null (empty response body)

### Authorization

[AdminToken](../README.md#AdminToken), [UserToken](../README.md#UserToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

<a name="userUserIdOrdersDeliveringGet"></a>
# **userUserIdOrdersDeliveringGet**
> List userUserIdOrdersDeliveringGet(user\_id)



### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **user\_id** | **UUID**| Identifying the user. | [default to null] |

### Return type

[**List**](../Models/Order.md)

### Authorization

[AdminToken](../README.md#AdminToken), [UserToken](../README.md#UserToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: orders

<a name="userUserIdOrdersRequestingGet"></a>
# **userUserIdOrdersRequestingGet**
> List userUserIdOrdersRequestingGet(user\_id)



### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **user\_id** | **UUID**| Identifying the user. | [default to null] |

### Return type

[**List**](../Models/Order.md)

### Authorization

[AdminToken](../README.md#AdminToken), [UserToken](../README.md#UserToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: orders

<a name="usersLoginGet"></a>
# **usersLoginGet**
> UUID usersLoginGet()

Log in a user.

### Parameters
This endpoint does not need any parameter.

### Return type

**UUID**

### Authorization

[UserAuth](../README.md#UserAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: user_id

<a name="usersRegisterPost"></a>
# **usersRegisterPost**
> usersRegisterPost(email, password, name, phone\_number)

Create a new user.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **email** | **String**| Email of the user to create. | [default to null] |
| **password** | **String**| Password used for user to sign-in with. | [default to null] |
| **name** | **String**| Name of the new user. | [default to null] |
| **phone\_number** | **String**| Phone number of the new user. | [optional] [default to null] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

