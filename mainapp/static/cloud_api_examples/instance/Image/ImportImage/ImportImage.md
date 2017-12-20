### 阿里文档与项目文档差别

API描述中，阿里文档DiskDeviceMapping.n的n取值为[1, 16]。n 为 1 时表示系统盘，n 为 [2, 16] 时表示数据盘。
项目文档中DiskDeviceMapping.N 暂时只支持1，也就是只支持系统盘镜像，暂时不支持数据盘做镜像。

项目文档中，请求参数ClientToken在阿里文档中未出现
