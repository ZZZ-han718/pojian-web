# B站破茧探索（在线版）

选标签 → 按新奇度排序 B 站全站热门；懒得选 → 随便推。
浏览器直接调 B 站接口会被 CORS 和防盗链挡住，所以用两个无函数做转发。

## 目录结构

```
pojian-web/
├── index.html        页面本身（静态，Vercel 直接托管）
├── tip.jpg           打赏码图片（上传前自己放进来）
├── requirements.txt  无函数依赖
└── api/
    ├── bili.py       /api/bili?path=x/web-interface/popular  → 转发 B 站 API
    └── img.py        /api/img?url=...                       → 转发封面图
```

## 部署步骤（Vercel）

### 准备
1. 把你的收款码图片命名为 `tip.jpg`，放到本文件夹（和 index.html 同级）。
2. 注册一个 Vercel 账号：https://vercel.com （GitHub 或邮箱都行，免费）。

### 方式 A：网页上传（最简单，不用装任何东西）
1. 把这个文件夹压缩或直接新建一个 GitHub 仓库上传。
2. 打开 https://vercel.com/new ，选中这个仓库 → 点 **Deploy**。
3. 等 1 分钟，拿到 `https://你的项目名.vercel.app`。完成。

### 方式 B：命令行
```bash
# 先装好 Node.js：https://nodejs.org
npm i -g vercel
cd pojian-web
vercel login
vercel --prod
```

## 上线后要测的三件事
1. 打开首页 → 点「🎯 按兴趣排序全站热门」→ 出 20 条视频，封面正常显示。
2. 点封面能跳转到 B 站。
3. 拉到底部，能看到作者信息和打赏码。

## 可能踩的坑
- **接口返回「请求错误」**：Vercel 的机房 IP 可能被 B 站风控。一般加请求头就够了；
  真被拦时，把项目里的区域换到离用户近的节点（Vercel 默认机房在美国，可在
  项目设置里调整），或换 Cloudflare Workers 重写一版。
- **免费额度**：Hobby 套餐个人用完全够，每月 10 万次无函数调用，不会超。
- **想换地址**：Vercel 项目设置里可以改成 `xxx.vercel.app` 的名字，或绑定自己的域名。
