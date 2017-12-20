### 阿里文档与项目文档差别

API描述差异较大

项目文档中，请求参数InternetMaxBandwi dthOut、InternetMaxBandwi dthIn的语义描述和阿里文档不一致；

项目文档中，请求参数缺少NetworkChargeType、AutoPay、ClientToken；

项目文档中缺少返回参数RequestId、OrderId

错误码表中差异见下表，其他部分一致

|阿里文档|项目文档|
|:-:|:-:|
|Account.Arrearage||
|DecreasedBandWidthNotAllowed||
|InvalidEndTime.ValueNotSupported||
|InvalidInstance.UnpaidOrder||
|InvalidInstanceStatus.NotStopped||
|InvalidInternetChargeType.ValueNotSupported||
|InvalidInternetMaxBandwidthIn.ValueNotSupported|InvalidInternetMaxBandwidthIn.ValueNotSupported|
|InvalidInternetMaxBandwidthOut.ValueNotSupported|InvalidInternetMaxBandwidthOut.ValueNotSupported|
|InvalidStartTime.ValueNotSupported||
|MissingParameter|MissingParameter|
|OperationDenied||
|ChargeTypeViolation|ChargeTypeViolation|
|IncorrectInstanceStatus|IncorrectInstanceStatus|
|InstanceExpiredOrInArrears|InstanceExpiredOrInArrears|
|InstanceLockedForSecurity|InstanceLockedForSecurity|
|InvalidAccountStatus.NotEnoughBalance||
|OperationDenied||
|InvalidInstanceId.NotFound|InvalidInstanceId.NotFound|
|InternalError|InternalError|
||InvalidParameter|
||InvalidParameter|
