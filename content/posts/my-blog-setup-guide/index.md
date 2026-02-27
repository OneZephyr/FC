---
title: "从零到一：我的高颜值数字花园搭建全记录"
date: 2026-02-27T21:35:47+08:00
draft: false
description: "记录使用 Trae Solo, Hugo (Blowfish), GitHub Pages 和 Cloudflare 打造极致静态博客的过程。"
summary: "这不仅是一个博客，更是一个自动化的技术堡垒。从 AI 辅助开发到全球加速，我在这里记录了每一个踩坑与起飞的瞬间。"
feature: "cover.jpg" # 记得在该文件夹下放一张封面图
showTableOfContents: true
showComments: true
tags: ["Hugo", "Trae", "Blog", "Cloudflare"]
categories: ["技术分享"]
---

## 缘起：为什么选择这条路？

在碎片化信息时代，拥有一个完全自主、美观且响应迅速的个人站点是一种浪漫。我选择了：
* **Hugo (Blowfish)**：极致的性能与现代感。
* **Trae Solo**：AI 辅助开发，让配置不再枯燥。
* **GitHub + Cloudflare**：双重保险，全球加速。

## 核心架构图



## 关键技术点复盘

### 1. 自动化部署的“特殊处理”
很多初学者纠结于 Hugo 生成的 `public` 文件夹路径问题。我通过 **GitHub Actions** 实现了源码即发布的流程：
- 只上传源码，由 GitHub 在云端执行 `hugo --minify`。
- 自动将构建产物投递到 GitHub Pages 和 Cloudflare Pages。

### 2. 颜值即正义
利用 Blowfish 的 **毛玻璃效果 (Glassmorphism)** 和 **背景图** 配置，我调整了全站的色调：
```toml
[appearance]
  colorScheme = "ocean"
  cardAlpha = 0.9
```

### 3. 持久化与加速
为了保证 fc.181861.xyz 在全球范围内秒开，我接入了 Cloudflare，并开启了 Always Online 和 Edge Cache。即便源站波动，缓存依然能让内容时刻在线。

互动与功能
现在的站点已经集成了：

Giscus：基于 GitHub Discussions 的评论系统。

Algolia：毫秒级的全文搜索。

运行统计：记录这个数字生命诞生的每一秒。

结语
这只是个开始。在这个花园里，我会继续记录技术、生活和那些闪光的瞬间。

如果你对我的搭建过程感兴趣，欢迎在下方评论区交流！