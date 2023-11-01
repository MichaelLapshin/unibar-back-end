# DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adminLoginPost**](DefaultApi.md#adminLoginPost) | **POST** /admin/login | 
[**adminMessagesListGet**](DefaultApi.md#adminMessagesListGet) | **GET** /admin/messages/list | 
[**adminOrdersListGet**](DefaultApi.md#adminOrdersListGet) | **GET** /admin/orders/list | 
[**adminReportsListGet**](DefaultApi.md#adminReportsListGet) | **GET** /admin/reports/list | 
[**adminUsersListGet**](DefaultApi.md#adminUsersListGet) | **GET** /admin/users/list | 
[**deploymentGet**](DefaultApi.md#deploymentGet) | **GET** /deployment | 
[**messagePost**](DefaultApi.md#messagePost) | **POST** /message | 
[**orderCancelPut**](DefaultApi.md#orderCancelPut) | **PUT** /order/cancel | 
[**orderClaimPut**](DefaultApi.md#orderClaimPut) | **PUT** /order/claim | 
[**orderCompletePut**](DefaultApi.md#orderCompletePut) | **PUT** /order/complete | 
[**orderCreatePost**](DefaultApi.md#orderCreatePost) | **POST** /order/create | 
[**orderOrderIdGet**](DefaultApi.md#orderOrderIdGet) | **GET** /order/{order_id} | 
[**orderReportPost**](DefaultApi.md#orderReportPost) | **POST** /order/report | 
[**orderUnclaimPut**](DefaultApi.md#orderUnclaimPut) | **PUT** /order/unclaim | 
[**ordersAvailableGet**](DefaultApi.md#ordersAvailableGet) | **GET** /orders/available | 
[**pingGet**](DefaultApi.md#pingGet) | **GET** /ping | 
[**shutdownGet**](DefaultApi.md#shutdownGet) | **GET** /shutdown | 
[**userIdGet**](DefaultApi.md#userIdGet) | **GET** /user/id | 
[**userUserIdGet**](DefaultApi.md#userUserIdGet) | **GET** /user/{user_id} | 
[**userUserIdOrdersActiveGet**](DefaultApi.md#userUserIdOrdersActiveGet) | **GET** /user/{user_id}/orders/active | 
[**userUserIdOrdersClaimedGet**](DefaultApi.md#userUserIdOrdersClaimedGet) | **GET** /user/{user_id}/orders/claimed | 
[**userUserIdUpdatePatch**](DefaultApi.md#userUserIdUpdatePatch) | **PATCH** /user/{user_id}/update | 
[**usersLoginPost**](DefaultApi.md#usersLoginPost) | **POST** /users/login | Log in a user. Set cookie auth token.
[**usersLogoutGet**](DefaultApi.md#usersLogoutGet) | **GET** /users/logout | 
[**usersRegisterPost**](DefaultApi.md#usersRegisterPost) | **POST** /users/register | Create a new user.


<a name="adminLoginPost"></a>
# **adminLoginPost**
> adminLoginPost(bodyAdminLogin)



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bodyAdminLogin** | [**BodyAdminLogin**](..//Models/BodyAdminLogin.md)|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

<a name="adminMessagesListGet"></a>
# **adminMessagesListGet**
> List adminMessagesListGet()



### Parameters
This endpoint does not need any parameter.

### Return type

[**List**](..//Models/Message.md)

### Authorization

[AdminAuth](../README.md#AdminAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="adminOrdersListGet"></a>
# **adminOrdersListGet**
> List adminOrdersListGet()



### Parameters
This endpoint does not need any parameter.

### Return type

[**List**](..//Models/Order.md)

### Authorization

[AdminAuth](../README.md#AdminAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="adminReportsListGet"></a>
# **adminReportsListGet**
> List adminReportsListGet()



### Parameters
This endpoint does not need any parameter.

### Return type

[**List**](..//Models/Report.md)

### Authorization

[AdminAuth](../README.md#AdminAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="adminUsersListGet"></a>
# **adminUsersListGet**
> List adminUsersListGet()



### Parameters
This endpoint does not need any parameter.

### Return type

[**List**](..//Models/User.md)

### Authorization

[AdminAuth](../README.md#AdminAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="deploymentGet"></a>
# **deploymentGet**
> String deploymentGet()



### Parameters
This endpoint does not need any parameter.

### Return type

[**String**](..//Models/string.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain

<a name="messagePost"></a>
# **messagePost**
> messagePost(bodyMessage)



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bodyMessage** | [**BodyMessage**](..//Models/BodyMessage.md)|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

<a name="orderCancelPut"></a>
# **orderCancelPut**
> orderCancelPut(bodyOrderCancel)



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bodyOrderCancel** | [**BodyOrderCancel**](..//Models/BodyOrderCancel.md)|  |

### Return type

null (empty response body)

### Authorization

[UserAuth](../README.md#UserAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

<a name="orderClaimPut"></a>
# **orderClaimPut**
> orderClaimPut(bodyOrderClaim)



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bodyOrderClaim** | [**BodyOrderClaim**](..//Models/BodyOrderClaim.md)|  |

### Return type

null (empty response body)

### Authorization

[UserAuth](../README.md#UserAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

<a name="orderCompletePut"></a>
# **orderCompletePut**
> orderCompletePut(bodyOrderComplete)



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bodyOrderComplete** | [**BodyOrderComplete**](..//Models/BodyOrderComplete.md)|  |

### Return type

null (empty response body)

### Authorization

[UserAuth](../README.md#UserAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

<a name="orderCreatePost"></a>
# **orderCreatePost**
> orderCreatePost(bodyOrderRequest)



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bodyOrderRequest** | [**BodyOrderRequest**](..//Models/BodyOrderRequest.md)|  |

### Return type

null (empty response body)

### Authorization

[UserAuth](../README.md#UserAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

<a name="orderOrderIdGet"></a>
# **orderOrderIdGet**
> Order orderOrderIdGet(orderId)



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orderId** | [**UUID**](..//Models/.md)| The ID of the order which the client wants to see its info. | [default to null]

### Return type

[**Order**](..//Models/Order.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="orderReportPost"></a>
# **orderReportPost**
> orderReportPost(bodyOrderReport)



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bodyOrderReport** | [**BodyOrderReport**](..//Models/BodyOrderReport.md)|  |

### Return type

null (empty response body)

### Authorization

[UserAuth](../README.md#UserAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

<a name="orderUnclaimPut"></a>
# **orderUnclaimPut**
> orderUnclaimPut(bodyOrderUnclaim)



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bodyOrderUnclaim** | [**BodyOrderUnclaim**](..//Models/BodyOrderUnclaim.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

[UserAuth](../README.md#UserAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

<a name="ordersAvailableGet"></a>
# **ordersAvailableGet**
> List ordersAvailableGet()



### Parameters
This endpoint does not need any parameter.

### Return type

[**List**](..//Models/Order.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="pingGet"></a>
# **pingGet**
> String pingGet()



### Parameters
This endpoint does not need any parameter.

### Return type

[**String**](..//Models/string.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain

<a name="shutdownGet"></a>
# **shutdownGet**
> shutdownGet()



### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[AdminAuth](../README.md#AdminAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

<a name="userIdGet"></a>
# **userIdGet**
> userIdGet()



### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[UserAuth](../README.md#UserAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

<a name="userUserIdGet"></a>
# **userUserIdGet**
> User userUserIdGet(userId)



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userId** | [**UUID**](..//Models/.md)| User ID of the user to identify who&#39;s info to get. | [default to null]

### Return type

[**User**](..//Models/User.md)

### Authorization

[AdminAuth](../README.md#AdminAuth), [UserAuth](../README.md#UserAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="userUserIdOrdersActiveGet"></a>
# **userUserIdOrdersActiveGet**
> List userUserIdOrdersActiveGet(userId)



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userId** | [**UUID**](..//Models/.md)| User ID of which we want to see the orders they are currently requesting. | [default to null]

### Return type

[**List**](..//Models/Order.md)

### Authorization

[AdminAuth](../README.md#AdminAuth), [UserAuth](../README.md#UserAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="userUserIdOrdersClaimedGet"></a>
# **userUserIdOrdersClaimedGet**
> List userUserIdOrdersClaimedGet(userId)



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userId** | [**UUID**](..//Models/.md)| User ID of which we want to see the orders they are currently claiming. | [default to null]

### Return type

[**List**](..//Models/Order.md)

### Authorization

[AdminAuth](../README.md#AdminAuth), [UserAuth](../README.md#UserAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="userUserIdUpdatePatch"></a>
# **userUserIdUpdatePatch**
> userUserIdUpdatePatch(userId, bodyUserUpdate)



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userId** | [**UUID**](..//Models/.md)| User ID of user we are trying to update. | [default to null]
 **bodyUserUpdate** | [**BodyUserUpdate**](..//Models/BodyUserUpdate.md)|  |

### Return type

null (empty response body)

### Authorization

[AdminAuth](../README.md#AdminAuth), [UserAuth](../README.md#UserAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

<a name="usersLoginPost"></a>
# **usersLoginPost**
> UUID usersLoginPost(bodyUsersLogin)

Log in a user. Set cookie auth token.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bodyUsersLogin** | [**BodyUsersLogin**](..//Models/BodyUsersLogin.md)|  |

### Return type

[**UUID**](..//Models/UUID.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="usersLogoutGet"></a>
# **usersLogoutGet**
> usersLogoutGet()



### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[UserAuth](../README.md#UserAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

<a name="usersRegisterPost"></a>
# **usersRegisterPost**
> usersRegisterPost(bodyUsersRegister)

Create a new user.

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bodyUsersRegister** | [**BodyUsersRegister**](..//Models/BodyUsersRegister.md)|  |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

