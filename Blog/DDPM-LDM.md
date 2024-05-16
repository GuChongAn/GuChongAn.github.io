---
name: [Read Paper] DDPM 和 LDM 两篇扩散模型的论文
date: 20240516
description: 精读了DDPM和LDM两篇扩散模型的论文
keywords: readpaper
---

按照之前计划，打算读扩散模型相关的两篇文章，

- [Denoising Diffusion Probabilistic Models](https://arxiv.org/abs/2006.11239)（DDPM）
- [High-Resolution Image Synthesis with Latent Diffusion Models](https://arxiv.org/abs/2112.10752)（LDM）

结果读的时候发现这两篇文章，特别是前者，数学上的东西比较多，缺了一些基础知识，读起来有些困难，所以和之前总结式的笔记不同，这次计划做一次精读，先来看Denoising Diffusion Probabilistic Models这篇文章，

## [NeurIPS] Denoising Diffusion Probabilistic Models

### Abstract

> We present high quality image synthesis results using diffusion probabilistic models, a class of latent variable models inspired by considerations from nonequilibrium thermodynamics. 

latent variable model，就是计算latent变量的模型，以问卷举例，显式变量是问卷中问题的答案，隐式变量就是我们问问卷想要调查的那个问题，也有点类似全连接神经网络中隐藏层的意思

> Our best results are obtained by training on a weighted variational bound designed according to a novel connection between diffusion probabilistic models and denoising score matching with Langevin dynamics, and our models naturally admit a progressive lossy decompression scheme that can be interpreted as a generalization of autoregressive decoding. 

weighted variational bound，联系后文，就是**xxx**

denoising score matching with Langevin dynamics，联系后文，就是**xxx**

autoregressive decoding，Transformer也是自回归模型，一步一步迭代计算结果

所谓渐进有损压缩策略可以解释为自回归模型的泛化，意思是**xxx**

### 1 Introduction

> ...... there have been remarkable advances in energy-based modeling and score matching that have produced images comparable to those of GANs. 

energy-based modeling，一类生成模型的总称

> ...... A diffusion probabilistic model is a parameterized Markov chain trained using variational inference to produce samples matching the data after finite time. 

Markov chain，就是一组随机过程，满足某一项的概率只与它的前一项相关，即
$$
P(X_{t}|X_{t-1}X_{t-2}...X_0) = P(X_t|X_{t-1})
$$
variational inference，原本要求分布p，但是p不好求，就把问题分解为，1）找到和p相近的分布q，2）把q优化为p

> ...... it is sufficient to set the sampling chain transitions to conditional Gaussians too

conditional Gaussians，高斯分布就是正态分布，条件高斯分布就是对于一个多元高斯分布，在已知一些值的情况下，其余变量的高斯分布

> ...... an equivalence with denoising score matching over multiple noise levels during training and with annealed(退火) Langevin dynamics during sampling. 

在训练过程中多个噪声级别上的去噪分数匹配和在采样过程中郎之万动力学的等价性，

### 2 Background
