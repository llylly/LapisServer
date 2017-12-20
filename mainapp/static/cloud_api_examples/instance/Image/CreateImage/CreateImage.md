### 阿里文档与项目文档差别

API描述部分差别较大

项目文档中，请求参数缺少InstanceId、DiskDeviceMapping.N.Size、DiskDeviceMapping.N.SnapshotId；

错误码表中差异见下表，其他部分一致

|阿里文档|项目文档|
|:-:|:-:|
|IncorrectInstanceStatus||
|InstanceLockedForSecurity||
|InvalidDescription.Malformed|InvalidDescription.Malformed|
|InvalidImageName.Duplicated||
|InvalidImageName.Malformed|InvalidImageName.Malformed|
|InvalidImageVersion.Malformed|InvalidImageVersion.Malformed|
|InvalidInstanceId.NotFound||
|InvalidInstanceId.ValueNotSupported||
|InvalidSize.ValueNotSupported||
|MissingParameter|MissingParameter|
|OperationDenied|OperationDenied|
|OperationDenied|OperationDenied|
|InvalidAccountStatus.NotEnoughBalance||
|InvalidAccountStatus.SnapshotServiceUnavailable||
|InvalidParamter.Conflict|InvalidParamter.Conflict|
|InvalidSnapshot.TooOld|InvalidSnapshot.TooOld|
|InvalidSnapshotId.NotReady|InvalidSnapshotId.NotReady|
|OperationDenied||
|OperationDenied||
|QuotaExceed.Image|QuotaExceed.Image|
|InvalidRegionId.NotFound|InvalidRegionId.NotFound|
|InvalidSnapshotId.NotFound|InvalidSnapshotId.NotFound|
|InvalidSnapshotId.NotFound||
||MissingParameter|

### lapis建议

lapis建议请求参数DiskDeviceMapping.N.Size类型改为integer，以更好地描述取值范围：[5, 2000]