

## AllocateEipAddress

### 阿里文档与项目文档差异

项目文档中，请求参数缺少InstanceChargeType、PricingCycle，Period，AutoPay；

项目文档中，返回参数缺少OrderId；

### lapis建议

请求参数PricingCycle使用integer类型，可以更好地描述取值范围

## AssociateEipAddress

### 阿里文档与项目文档差异

项目文档中，API描述部分有差异；

项目文档中，请求参数InstanceType、InstanceId的语义描述与阿里文档有差异；


## DescribeEipAddresses

### 阿里文档与项目文档差异

项目文档中，请求参数AssociatedInstanceType、AssociatedInstanceId的语义描述与阿里文档有差异；


## UnassociateEipAddress

### 阿里文档与项目文档差异

项目文档中，API描述部分有差异；

项目文档中，请求参数InstanceType、InstanceId的语义描述与阿里文档有差异；



## DescribeBandwidthPackageMonitorData

### 项目文档与阿里文档的差异

yaml以项目文档为准

### 文档勘误

阿里文档与项目文档中，此API未在API列表中出现

## DescribeBandwidthPackagePublicIpMonitorData

### 文档勘误

阿里文档与项目文档中，此API未在API列表中出现

## AddBandwidthPackageIps

### 项目文档与阿里文档的差异

项目文档中，API描述部分和阿里文档有差异

## CreateBandwidthPackage

### 项目文档与阿里文档的差异

项目文档中，API描述部分和阿里文档有差异

### 文档勘误

阿里文档与项目文档中，此API未在API列表中出现


## CreateForwardEntry

### 项目文档与阿里文档的差异

阿里文档中使用DNAT来表示端口转发规则；

项目文档中，API描述部分和阿里文档有差异；

项目文档中，请求参数ExternalIp的语义描述和阿里文档不一致；

阿里文档用公网私网来表示源端和目的端


### lapis建议

建议请求参数ExternalPort，InternalPort类型修改为integer，以更好地描述取值范围

## CreateNatGateway

### 项目文档与阿里文档的差异

项目文档中，API描述部分和阿里文档有差异；

项目文档中，请求参数BandwidthPackage.n.IpCount、BandwidthPackage.n.Bandwidth的、BandwidthPackage.n.Zone“是否必须”和“描述”两栏的内容与阿里文档有差异；


## CreateSnatEntry

### 项目文档与阿里文档的差异

项目文档中，API描述部分和阿里文档有差异；

阿里文档与项目文档中，此API未在API列表中出现；

项目文档中，请求参数缺少SourceCIDR；

项目文档中，请求参数SnatIp的语义描述和阿里文档有差异


### 文档勘误

阿里文档与项目文档中，此API未在API列表中出现

## DeleteBandwidthPackage

### 项目文档与阿里文档的差异

项目文档中，API描述部分和阿里文档有差异

## DeleteForwardEntry

### 项目文档与阿里文档的差异

阿里文档中使用DNAT来表示端口转发规则；

项目文档中，API描述部分和阿里文档有差异；

## DeleteSnatEntry

### 文档勘误

阿里文档与项目文档中，此API未在API列表中出现

## DescribeBandwidthPackages

### 项目文档与阿里文档的差异

项目文档中，API描述部分和阿里文档有差异


## DescribeForwardTableEntries

### 项目文档与阿里文档的差异

阿里文档中使用DNAT来表示端口转发规则

## DescribeSnatTableEntries

### 文档勘误

阿里文档与项目文档中，此API未在API列表中出现

## ModifyBandwidthPackageAttribute

### 项目文档与阿里文档的差异

阿里文档中API描述有“本接口仅支持在2017年11月3日23:59之前账户下存在NAT带宽包的用户调用。2017年11月3日23:59之前账户下不存在NAT带宽包的用户请参考绑定弹性公网IP，在NAT网关上绑定弹性公网IP。”，项目文档中则没有


## ModifyBandwidthPackageSpec

### 项目文档与阿里文档的差异

项目文档中，API描述部分和阿里文档有差异

### lapis建议

建议请求参数Bandwidth的类型为integer，以更好地描述取值范围

## ModifyForwardEntry

### 项目文档与阿里文档的差异

阿里文档中使用DNAT来表示端口转发规则；

项目文档中，API描述部分和阿里文档有差异；

项目文档中，请求参数ExternalIp的语义描述和阿里文档不一致；

阿里文档用公网私网来表示源端和目的端

### lapis建议

建议请求参数ExternalPort，InternalPort类型修改为integer，以更好地描述取值范围

## ModifyNatGatewayAttribute

### 阿里文档与项目文档的差异

项目文档中，API描述部分和阿里文档有差异


### 文档勘误

阿里文档与项目文档中，此API未在API列表中出现

## ModifyNatGatewaySpec

### 文档勘误

阿里文档与项目文档中，此API未在API列表中出现

## ModifySnatEntry

### 项目文档与阿里文档的差异

项目文档中，API描述部分和阿里文档有差异；

阿里文档与项目文档中，此API未在API列表中出现；

项目文档中，请求参数SnatIp的语义描述和阿里文档有差异


### 文档勘误d

阿里文档与项目文档中，此API未在API列表中出现

## RemoveBandwidthPackageIps

### 项目文档与阿里文档的差异

项目文档中，API描述部分和阿里文档有差异；

项目文档中，请求参数RemovedIpAddress es.n的语义描述与阿里文档有差异；


## CreatePhysicalConnection

### lapis建议

建议请求参数Bandwidth的类型为integer，以更好地描述取值范围

## DescribePhysicalConnections

### 阿里文档与项目文档差别

项目文档中，请求参数PageSize的语义描述和阿里文档有差异

## ModifyPhysicalConnectionAttribute

### lapis建议

建议请求参数Bandwidth的类型为integer，以更好地描述取值范围

## DescribeAccessPoints

### 文档勘误

阿里文档与项目文档中，此API未在API列表中出现

## CreateRouteEntry

### 阿里文档与项目文档差别

阿里文档在API描述部分追加了一些描述

## DeleteRouteEntry

### 阿里文档与项目文档差别

API描述部分和阿里文档有差异

## DescribeVirtualBorderRouters

### 阿里文档与项目文档差别

项目文档中，请求参数PageSize的语义描述和阿里文档有差异


## ModifyVirtualBorderRouterAttribute

### 阿里文档与项目文档差别

请求参数VBRName、VBRDescription的名称和阿里文档有差异


## CreateVpc

### 阿里文档与项目文档差异

项目文档中，API描述部分- 每个 VPC 包含的云产品实例数量不超过 5000 个，阿里文档中是不超过10000个



## DeleteVpc

### 阿里文档与项目文档差异

项目文档中，API描述部分- 每个 VPC 包含的云产品实例数量不超过 5000 个，阿里文档中是不超过10000个

项目文档中，请求参数VpcId的语义描述与阿里文档有差异


## CreateVSwitch

### 阿里文档与项目文档差异

项目文档中，API描述部分- VSwitch 下的云产品实例数量不允许超过 VPC 剩余的可用云产品实例数量（5000 - 当前云产品实例数量），阿里文档中是10000

## DescribeVSwitches

### 阿里文档与项目文档差异

项目文档中，请求参数缺少RegionId

