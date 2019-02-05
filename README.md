---
layout: docs
title: Resolvers
---

# Overview

This is a set of resolvers to retrieve additional information about
the current stack and make it available to jinja templates.

## Available Resolvers

### stack_name

Fetches the current stack name.

Syntax:

```yaml
parameter|sceptre_user_data:
    <name>: !stack_name
```

Examples:

```
sceptre_user_data:
    stackenv: !stack_name
```


### stack_env

Fetches the current stack configuration environment name.

Syntax:

```yaml
parameter|sceptre_user_data:
    <name>: !stack_env
```

Examples:

```yaml
sceptre_user_data:
    stackenv: !stack_env
```

## Usage

### Definitions

config/dev/buckets.yaml:

```yaml
template_path: buckets.j2
stack_name: mystack
sceptre_user_data:
  stackname: !stack_name
  stackenv: !stack_env
  buckets_count: 4
  bucket_name_prefix: mybucket
```

templates/buckets.j2:
```
{# Jinja template to deploy multiple buckets #}

AWSTemplateFormatVersion: '2010-09-09'
Description: S3 buckets
Resources:
{% for n in range(sceptre_user_data.buckets_count|int) %}
  {{ sceptre_user_data.stackenv }}S3Bucket{{ loop.index }}:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: {{ sceptre_user_data.stackenv }}-{{ sceptre_user_data.stackenv }}-{{ sceptre_user_data.bucket_name_prefix }}-{{ loop.index }}
{% endfor %}
```


### Run

```bash
sceptre --output yaml generate dev/buckets.yaml
```

### Output

```yaml
  AWSTemplateFormatVersion: '2010-09-09'
  Description: S3 buckets
  Resources:
    mystackS3Bucket1:
      Properties:
        BucketName: mystack-dev-mybucket-1
      Type: AWS::S3::Bucket
    mystackS3Bucket2:
      Properties:
        BucketName: mystack-dev-mybucket-2
      Type: AWS::S3::Bucket
    mystackS3Bucket3:
      Properties:
        BucketName: mystack-dev-mybucket-3
      Type: AWS::S3::Bucket
    mystackS3Bucket4:
      Properties:
        BucketName: mystack-dev-mybucket-4
      Type: AWS::S3::Bucket
```
