### 阿里文档与项目文档差别

关于最长查询的天数，阿里和项目文档的API描述存在差异；

错误码表中差异见下表，其他部分一致

|阿里文档|项目文档|
|:-:|:-:|
|InvalidDiskId.NotFound|InvalidDiskId.NotFound|
|InvalidStartTime.Malformed|InvalidStartTime.Malformed|
|InvalidEndTime.Malformed|InvalidEndTime.Malformed|
|InvalidPeriod.ValueNotSupported|InvalidPeriod.ValueNotSupported|
|InvalidStartTime.TooEarly|InvalidStartTime.TooEarly|
|InvalidParameter.TooManyDataQueried||
|Throttling||
||MissingParameter|
||MissingParameter|
||MissingParameter|
||InvalidParameter|
