
-목표 정확도(손실값) 설정
 > 최근 발표된 논문 10개 정도 선정해 평균적인 정확도/손실 확인
 > 학회지 등 참고해서 목표를 설정해라
> 워크 분류 체계(WBS) 만들기

- 개선 아이디어
v1 만들기(weak augmentation만 넣기)
 > 최적 모델, optimizer, 손실함수 찾기
v2 분할(medium augmentation)
 > 검증해보고, 결과 개선

v2.RandomHorizontalFlip(p=0.5),
    v2.RandAugment(num_ops=2, magnitude=7),
    v2.RandomResizedCrop(size=(92, 92), scale=(0.8, 1.0)),

v3 가능하면(strong augmentation+alpha 해보기)

>>개선 아이디어
코드 모듈화 해보기

1. early stopping 추가
2. train/val transform 분리
3. epoch 증가
4. 
>> 이미지 데이터 전처리 관련 정리할 것!