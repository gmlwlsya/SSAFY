
# 📅 진행 기간

**2026.08.04 ~ 2026.08.31**



# 📚 목차

## 0. Python for AI

* **기초 준비**: AI 학습 전 참고 자료 (`00_lectures` - 실습 1, 2, 3)
* **핵심 역량**: Python 기본 문법, EDA(탐색적 데이터 분석), 데이터 시각화 및 머신러닝 기본 라이브러리 활용



## 1. AI & 기계학습 기초

* **지도학습 (Supervised Learning)**: 입력($X$)과 정답 라벨($Y$)을 함께 학습하여 미지의 데이터 예측
* **회귀 (Regression)**: 연속형 수치 예측 / `MSE`, `RMSE`, `R²(결정계수)`
* **분류 (Classification)**: 범주형 카테고리 예측 / `Confusion Matrix`, `Accuracy`, `Precision`, `Recall`, `F1-Score`, `Cross-Entropy`


* **비지도학습 (Unsupervised Learning)**: 정답 라벨($Y$) 없이 데이터($X$)의 숨겨진 패턴 및 구조 탐색
* **K-Means 클러스터링**: 거리 기반(Distance-based) 군집화, `Centroid`, `K-Means++`
* **계층적 군집분석 (Hierarchical Clustering)**: 상향식(Agglomerative) 병합, `Dendrogram`





## 2. AI & 기계학습 방법론

* **선형 회귀 (Linear Regression)**: 입력과 출력 간의 선형 관계 모델링 ($Y = \beta_0 + \beta_1 X_1 + \dots + \beta_p X_p + \epsilon$)
* **최소제곱법 (OLS)**: 잔차제곱합(RSS) 최소화
* **통계적 유의성 평가**: `Coefficient(β)`, `Std. Error`, `t-statistic`, `p-value (< 0.05)`
* **주의사항**: `다중공선성(Multicollinearity)`, `상관관계 vs 인과관계`


* **로지스틱 회귀 (Logistic Regression)**: 확률 기반 이진 분류 모델
* **모델식**: `Sigmoid Function`, `Odds Ratio`, `Logit Transformation`
* **최적화**: `Likelihood`, `Log-Likelihood`, `MLE (최대우도추정법)`


* **신경망 모델 (Neural Networks)**: 비선형 패턴 학습 및 다층 구조
* **Shallow 네트워크**: 1개의 은닉층, `ReLU`, `Piecewise Linear`, `보편적 근사 정리`
* **Deep 네트워크**: 2개 이상의 은닉층, `Folding(접기) 효과`, `표현력(Efficiency)`
* **행렬 연산**: $\mathbf{h}^{(l)} = \text{ReLU}\left(\mathbf{W}^{(l)}\mathbf{h}^{(l-1)} + \mathbf{b}^{(l)}\right)$


* **신경망 적합 및 최적화 (Fitting & Optimization)**: 오차 최소화 알고리즘
* **손실함수 & 학습**: `Loss Function ($L[\boldsymbol{\phi}]$)`, `Argmin`
* **경사하강법 (Gradient Descent)**: `Gradient ($\nabla L$)`, `Learning Rate ($\alpha$)`, `Convex vs Non-Convex`
* **확률적 경사하강법 (SGD)**: `Mini-batch`, `Noise`, `Local Minima & Saddle Point 탈출`
* **역전파 (Backpropagation)**: `Chain Rule (연쇄 법칙)`, `체인 미분`





## 3. 워드 임베딩과 순환신경망 기반 모델 (RNN & LSTM)

* **자연어 처리 기초**: 원-핫 인코딩(One-Hot Encoding) 및 한계점, 워드 임베딩(Word Embedding), Word2Vec(CBOW, Skip-gram)
* **순환 신경망 모델**: 시퀀스 데이터 처리, RNN 기본 구조, 기울기 소실(Vanishing Gradient) 문제
* **LSTM & Seq2Seq**: LSTM (Cell State, 3가지 Gate), Seq2Seq 구조 및 Teacher Forcing / Beam Search
* **Attention & Transformer**: Attention Mechanism, Self-Attention(Q, K, V), Transformer 아키텍처 및 Positional Encoding
* **사전 학습 언어 모델 (LLM 기초)**: Encoder/Decoder 기반 모델(BERT, T5, GPT), In-Context Learning 및 CoT(Chain-of-Thought) 프롬프팅


<br>

*수식 때문에 미리보기에서는 문제 없이 보이는 내용이 ebook-html 으로 하면 깨짐
바로 브라우저로 열기 선택해서 ㄱㄱ