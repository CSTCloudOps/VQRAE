# Bi-VQRAE

The source code for paper “Anomaly Detection in Time Series with Robust
Variational Quasi-Recurrent Autoencoders”

## Abstract

We propose variational quasi-recurrent autoencoders (VQRAEs) to enable
robust and efficient anomaly detection in time series in unsupervised
settings. The proposed VQRAEs employs a judiciously designed objective
function based on robust divergences including alpha, beta, and
gamma-divergence, making it possible to separate anomalies from normal
data without the reliance on anomaly labels, thus achieving robustness
and fully unsupervised training. To better capture temporal dependencies
in time series data, VQRAEs are built upon quasi-recurrent neural
networks, which employ convolution and gating mechanisms to avoid the
inefficient recursive computations used by classic recurrent neural
networks. Further, VQRAEs can be extended to bi-directional BiVQRAEs
that utilize bi-directional information to further improve the accuracy.
The above design choices make VQRAEs not only robust and thus accurate,
but also efficient at detecting anomalies in streaming settings.
Experiments on five real-world time series offer insight into the design
properties of VQRAEs and demonstrate that VQRAEs are capable of
outperforming state-of-the-art methods.

## QRNN

<img src="https://latex.codecogs.com/svg.image?\begin{subequations}&space;&space;\begin{align}&space;&space;&space;&space;&space;&space;\mathbf{i}_{t}&space;&=&space;\mathsf{tanh}(\mathbf{W}^{1}_{\mathbf{i}}&space;\cdot&space;\mathbf{s}_{t-1}&space;&plus;&space;\mathbf{W}^{2}_{\mathbf{i}}&space;\cdot&space;\mathbf{s}_{t}&space;&plus;&space;\mathbf{b}_\mathbf{i})&space;\\&space;&space;&space;&space;&space;&space;\mathbf{f}_{t}&space;&=&space;\sigma(\mathbf{W}^{1}_{\mathbf{f}}&space;\cdot&space;\mathbf{s}_{t-1}&space;&plus;&space;\mathbf{W}^{2}_{\mathbf{f}}&space;\cdot&space;\mathbf{s}_{t}&space;&plus;&space;\mathbf{b}_\mathbf{f})&space;\\&space;&space;&space;&space;&space;&space;\mathbf{o}_{t}&space;&=&space;\sigma(\mathbf{W}^{1}_{\mathbf{o}}&space;\cdot&space;\mathbf{s}_{t-1}&space;&plus;&space;\mathbf{W}^{2}_{\mathbf{o}}&space;\cdot&space;\mathbf{s}_{t}&space;&plus;&space;\mathbf{b}_\mathbf{o})&space;\\&space;&space;&space;&space;&space;&space;\mathbf{c}_{t}&space;&=&space;\mathbf{f}_{t}&space;\odot&space;\mathbf{c}_{t-1}&space;&plus;&space;(1&space;-&space;\mathbf{f}_{t})&space;\odot&space;\mathbf{i}_{t}&space;\label{eqn:qrnn_4}\\&space;&space;&space;&space;&space;&space;\mathbf{h}_{t}&space;&=&space;\mathbf{o}_{t}&space;\odot&space;\mathbf{c}_{t}&space;&space;&space;\end{align}\end{subequations}" title="\begin{subequations} \begin{align} \mathbf{i}_{t} &= \mathsf{tanh}(\mathbf{W}^{1}_{\mathbf{i}} \cdot \mathbf{s}_{t-1} + \mathbf{W}^{2}_{\mathbf{i}} \cdot \mathbf{s}_{t} + \mathbf{b}_\mathbf{i}) \\ \mathbf{f}_{t} &= \sigma(\mathbf{W}^{1}_{\mathbf{f}} \cdot \mathbf{s}_{t-1} + \mathbf{W}^{2}_{\mathbf{f}} \cdot \mathbf{s}_{t} + \mathbf{b}_\mathbf{f}) \\ \mathbf{o}_{t} &= \sigma(\mathbf{W}^{1}_{\mathbf{o}} \cdot \mathbf{s}_{t-1} + \mathbf{W}^{2}_{\mathbf{o}} \cdot \mathbf{s}_{t} + \mathbf{b}_\mathbf{o}) \\ \mathbf{c}_{t} &= \mathbf{f}_{t} \odot \mathbf{c}_{t-1} + (1 - \mathbf{f}_{t}) \odot \mathbf{i}_{t} \label{eqn:qrnn_4}\\ \mathbf{h}_{t} &= \mathbf{o}_{t} \odot \mathbf{c}_{t} \end{align}\end{subequations}" />

## VQRAE

### qnet

<img src="https://latex.codecogs.com/svg.image?\begin{subequations}&space;\begin{align}&space;&space;&space;&space;&space;\mathbf{h}_{t}&space;&=&space;\mathsf{QRNN}(\mathbf{s}_{t-1},&space;\mathbf{s}_{t})&space;\\&space;&space;&space;&space;&space;\mathbf{a}_{t}&space;&=&space;\mathsf{QRNN}([\mathbf{s}_{t&plus;1},&space;\mathbf{h}_{t&plus;1}],&space;[\mathbf{s}_{t},&space;\mathbf{h}_{t}])&space;\\&space;&space;&space;&space;&space;\Phi_{\mathbf{z}_{t}}&space;&=&space;f(\mathbf{W}_{\Phi_{\mathbf{z}}}&space;\cdot&space;\mathbf{a}_{t}&space;&plus;&space;\mathbf{b}_{\Phi_{\mathbf{z}}})&space;\\&space;&space;&space;&space;&space;\mu_{\mathbf{z}_{t}}&space;&=&space;\mathbf{W}_{\mu_{\mathbf{z}}}&space;\cdot&space;\Phi_{\mathbf{z}_{t}}&space;&plus;&space;\mathbf{b}_{\mu_{\mathbf{z}}}&space;\\&space;&space;&space;&space;&space;\sigma_{\mathbf{z}_{t}}&space;&=&space;\mathsf{softplus}(\mathbf{W}_{\sigma_{\mathbf{z}}}&space;\cdot&space;\Phi_{\mathbf{z}_{t}}&space;&plus;&space;\mathbf{b}_{\sigma_{\mathbf{z}}})&space;&space;&space;\end{align}\end{subequations}" title="\begin{subequations} \begin{align} \mathbf{h}_{t} &= \mathsf{QRNN}(\mathbf{s}_{t-1}, \mathbf{s}_{t}) \\ \mathbf{a}_{t} &= \mathsf{QRNN}([\mathbf{s}_{t+1}, \mathbf{h}_{t+1}], [\mathbf{s}_{t}, \mathbf{h}_{t}]) \\ \Phi_{\mathbf{z}_{t}} &= f(\mathbf{W}_{\Phi_{\mathbf{z}}} \cdot \mathbf{a}_{t} + \mathbf{b}_{\Phi_{\mathbf{z}}}) \\ \mu_{\mathbf{z}_{t}} &= \mathbf{W}_{\mu_{\mathbf{z}}} \cdot \Phi_{\mathbf{z}_{t}} + \mathbf{b}_{\mu_{\mathbf{z}}} \\ \sigma_{\mathbf{z}_{t}} &= \mathsf{softplus}(\mathbf{W}_{\sigma_{\mathbf{z}}} \cdot \Phi_{\mathbf{z}_{t}} + \mathbf{b}_{\sigma_{\mathbf{z}}}) \end{align}\end{subequations}" />

<img src="q_net.png" alt="q_net" width="500" height="500" />

### pnet

<img src="https://latex.codecogs.com/svg.image?\begin{subequations}&space;&space;\begin{align}&space;&space;&space;&space;&space;&space;\Phi_{\mathbf{s}_{t}}&space;&=&space;f(\mathbf{W}_{\Phi_{\mathbf{s}}}&space;\cdot&space;[\mathbf{h}_{t},&space;\mathbf{z}_{t}]&space;&plus;&space;\mathbf{b}_{\Phi_{\mathbf{s}}})&space;\\&space;&space;&space;&space;&space;&space;\mu_{\mathbf{s}_{t}}&space;&=&space;\mathbf{W}_{\mu_{\mathbf{s}}}&space;\cdot&space;\Phi_{\mathbf{s}_{t}}&space;&plus;&space;\mathbf{b}_{\mu_{\mathbf{s}}}&space;\\&space;&space;&space;&space;&space;&space;\sigma_{\mathbf{s}_{t}}&space;&=&space;\mathsf{softplus}(\mathbf{W}_{\sigma_{\mathbf{s}}}&space;\cdot&space;\Phi_{\mathbf{s}_{t}}&space;&plus;&space;\mathbf{b}_{\sigma_{\mathbf{s}}})&space;&space;&space;\end{align}\end{subequations}" title="\begin{subequations} \begin{align} \Phi_{\mathbf{s}_{t}} &= f(\mathbf{W}_{\Phi_{\mathbf{s}}} \cdot [\mathbf{h}_{t}, \mathbf{z}_{t}] + \mathbf{b}_{\Phi_{\mathbf{s}}}) \\ \mu_{\mathbf{s}_{t}} &= \mathbf{W}_{\mu_{\mathbf{s}}} \cdot \Phi_{\mathbf{s}_{t}} + \mathbf{b}_{\mu_{\mathbf{s}}} \\ \sigma_{\mathbf{s}_{t}} &= \mathsf{softplus}(\mathbf{W}_{\sigma_{\mathbf{s}}} \cdot \Phi_{\mathbf{s}_{t}} + \mathbf{b}_{\sigma_{\mathbf{s}}}) \end{align}\end{subequations}" />

<img src="p_net.png" alt="q_net" width="500" height="500" />

## Objective Function

<img src="https://latex.codecogs.com/svg.image?\begin{equation}&space;&space;&space;&space;&space;argmax_{\phi,&space;\theta}\mathcal{L}(\mathbf{s}_{t})&space;&space;&space;&space;&space;=&space;\;&space;-&space;\mathbb{E}_{q_{\phi}(\mathbf{z}_{t}|\mathbf{s}_{t})}[\mathsf{D}_{\alpha,\beta,\gamma}(\hat{p}(\mathbf{s}_{t})||p_{\theta}(\mathbf{s}_{t}|\mathbf{z}_{t}))]&space;-&space;\mathsf{D_{KL}}[q_{\phi}(\mathbf{z}_{t}|\mathbf{s}_{t})||p_{\theta}(\mathbf{z}_{t})]\end{equation}" title="\begin{equation} argmax_{\phi, \theta}\mathcal{L}(\mathbf{s}_{t}) = \; - \mathbb{E}_{q_{\phi}(\mathbf{z}_{t}|\mathbf{s}_{t})}[\mathsf{D}_{\alpha,\beta,\gamma}(\hat{p}(\mathbf{s}_{t})||p_{\theta}(\mathbf{s}_{t}|\mathbf{z}_{t}))] - \mathsf{D_{KL}}[q_{\phi}(\mathbf{z}_{t}|\mathbf{s}_{t})||p_{\theta}(\mathbf{z}_{t})]\end{equation}" />

<img src="https://latex.codecogs.com/svg.image?\begin{equation}&space;\small&space;\begin{aligned}&space;&space;\mathsf{D}_\alpha(\hat{p}(\mathbf{s}_{t})||p_{\theta}(\mathbf{s}_{t}|\mathbf{z}_{t}))&space;&space;=&space;\frac{1}{\alpha&space;-&space;1}\mathsf{log}&space;&space;\int&space;\hat{p}(\mathbf{s}_{t})^{\alpha}p_{\theta}(\mathbf{s}_{t}|\mathbf{z}_{t})^{1&space;-&space;\alpha}d\mathbf{s}_{t}&space;\end{aligned}&space;\label{eqn:alpha_divergence}\end{equation}" title="\begin{equation} \small \begin{aligned} \mathsf{D}_\alpha(\hat{p}(\mathbf{s}_{t})||p_{\theta}(\mathbf{s}_{t}|\mathbf{z}_{t})) = \frac{1}{\alpha - 1}\mathsf{log} \int \hat{p}(\mathbf{s}_{t})^{\alpha}p_{\theta}(\mathbf{s}_{t}|\mathbf{z}_{t})^{1 - \alpha}d\mathbf{s}_{t} \end{aligned} \label{eqn:alpha_divergence}\end{equation}" />

<img src="https://latex.codecogs.com/svg.image?&space;\begin{align}\mathsf{D}_\beta(\hat{p}(\mathbf{s}_{t})||p_{\theta}(\mathbf{s}_{t}|\mathbf{z}_{t}))&space;&space;&space;&space;&space;=&space;&space;&space;&space;&space;&space;-&space;\frac{\beta&space;&plus;&space;1}{\beta}\int&space;\hat{p}(\mathbf{s}_{t})p_{\theta}(\mathbf{s}_{t}|\mathbf{z}_{t})^{\beta}d\mathbf{s}_{t}&space;&plus;&space;\frac{1}{\beta}\int&space;\hat{p}(\mathbf{s}_{t})^{\beta&space;&plus;&space;1}d\mathbf{s}_{t}&space;&plus;&space;\int&space;p_{\theta}(\mathbf{s}_{t}|\mathbf{z}_{t})^{\beta&space;&plus;&space;1}d\mathbf{s}_{t}&space;&space;\end{align}" title=" \begin{align}\mathsf{D}_\beta(\hat{p}(\mathbf{s}_{t})||p_{\theta}(\mathbf{s}_{t}|\mathbf{z}_{t})) = - \frac{\beta + 1}{\beta}\int \hat{p}(\mathbf{s}_{t})p_{\theta}(\mathbf{s}_{t}|\mathbf{z}_{t})^{\beta}d\mathbf{s}_{t} + \frac{1}{\beta}\int \hat{p}(\mathbf{s}_{t})^{\beta + 1}d\mathbf{s}_{t} + \int p_{\theta}(\mathbf{s}_{t}|\mathbf{z}_{t})^{\beta + 1}d\mathbf{s}_{t} \end{align}" />

<img src="https://latex.codecogs.com/svg.image?&space;\begin{align}&space;&space;\mathsf{D}_\gamma(\hat{p}(\mathbf{s}_{t})||p_{\theta}(\mathbf{s}_{t}|\mathbf{z}_{t}))&space;&space;=&space;&space;&space;-\frac{1}{\gamma}\mathsf{log}\int&space;\hat{p}(\mathbf{s}_{t})p_{\theta}(\mathbf{s}_{t}|\mathbf{z}_{t})^{\gamma}d\mathbf{s}_{t}&space;&plus;&space;\frac{1}{\gamma&space;(\gamma&space;&plus;&space;1)}\mathsf{log}\int&space;\hat{p}(\mathbf{s}_{t})^{\gamma&space;&plus;&space;1}d\mathbf{s}_{t}&space;&plus;&space;\frac{1}{\gamma&space;&plus;&space;1}\mathsf{log}\int&space;p_{\theta}(\mathbf{s}_{t}|\mathbf{z}_{t})^{\gamma&space;&plus;&space;1}d\mathbf{s}_{t}&space;&space;\end{align}" title=" \begin{align} \mathsf{D}_\gamma(\hat{p}(\mathbf{s}_{t})||p_{\theta}(\mathbf{s}_{t}|\mathbf{z}_{t})) = -\frac{1}{\gamma}\mathsf{log}\int \hat{p}(\mathbf{s}_{t})p_{\theta}(\mathbf{s}_{t}|\mathbf{z}_{t})^{\gamma}d\mathbf{s}_{t} + \frac{1}{\gamma (\gamma + 1)}\mathsf{log}\int \hat{p}(\mathbf{s}_{t})^{\gamma + 1}d\mathbf{s}_{t} + \frac{1}{\gamma + 1}\mathsf{log}\int p_{\theta}(\mathbf{s}_{t}|\mathbf{z}_{t})^{\gamma + 1}d\mathbf{s}_{t} \end{align}" />

## Citation

If you use the code, please cite the following paper:

```latex
@inproceedings{DBLP:conf/icde/KieuYGCZSJ22,
	author     = {Tung Kieu and Bin Yang and Chenjuan Guo and Razvan-Gabriel Cirstea and Yan Zhao and Yale Song and Christian S. Jensen},
	title      = {Anomaly Detection in Time Series with Robust Variational Quasi-Recurrent Autoencoders},
	booktitle  = {{ICDE}},
	pages      = {1--13},
	year       = {2022}
}
```
