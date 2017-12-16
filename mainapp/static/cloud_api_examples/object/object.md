## CreateCluster

### 文档差别

1）ecs_image_id 列表，项目文档表中额外多了地域；
2）请求体参数，项目文档少了io_optimized参数；
3）返回参数少了task_id

## UpdateClusterSizeById

### 文档差别

1）ecs_image_id 列表，项目文档表中额外多了地域；
2）请求体参数，项目文档少了io_optimized参数；


## Create project

### 文档差别

请求体参数，项目文档少了latest_image参数

### lapis 建议

environment类型为map，其中的key-value没有明确说明，建议将类型由map改为array，每一项为一个key-value对

## Delete project

### lapis 建议

变量名volume建议改为v，参数名在请求行中为v={volume},生成请求参数时使用 {变量名}={变量值}

## List Projects

### lapis 建议

environment类型为map，其中的key-value没有明确说明，建议将类型由map改为array，每一项为一个key-value对

## List Services

### lapis 建议

extensions，containers，definition类型为map，其中的key-value没有明确说明，建议将类型由map改为array，每一项为一个key-value对

## Retrieve project

### lapis 建议

将environment类型为map，其中的key-value没有明确说明，建议将类型由map改为array，每一项为一个key-value对

## Stop project

### lapis 建议

变量名timeout建议改为t，参数名在请求行中为t={timeout}

## Stop service

### lapis 建议

变量名timeout建议改为t，参数名在请求行中为t={timeout}

## Update project

### 文档差别

请求体参数，项目文档少了latest_image参数


### lapis 建议

environment类型为map，其中的key-value没有明确说明，建议将类型由map改为array，每一项为一个key-value对

## Scale project

### 文档差别

请求体格式不一样
