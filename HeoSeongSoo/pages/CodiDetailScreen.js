import React from  'react';
import { Text, TouchableWithoutFeedback, View, ScrollView } from 'react-native';
import Container from '../components/Container';
import axios from 'axios'
import styled from 'styled-components/native';


const CodiItemImg = styled.Image`
    width: 100%;
    height: 50%;
    resize-mode: cover;
`;

const TextContainer = styled.View`
    margin: 5px;
    justify-content: space-between;
`;

const ItemContainer = styled.View`
    margin: 5px;
    flex-direction: column;
`;

function CodiDetailScreen({ navigation, route }) {
    const [codiSetDetail, setCodiSetDetail] = React.useState(route.params.item)
    const [itemLike, setLikeItem] = React.useState({liked: route.params.item.liked, likes: route.params.item.likes})
    function changeHeart() {
        if (itemLike.liked){
            setLikeItem({
                liked: !itemLike.liked,
                likes: itemLike.likes - 1
            })
        } else {
            setLikeItem({
                liked: !itemLike.liked,
                likes: itemLike.likes + 1
            })
        }
        // axios 요청으로 하트 변경사항 저장
        // codiItem.id와 itemLike 전송
    }
    let nullCount = 0
    return (
        <Container>
            <Text>
                {codiSetDetail.user}
            </Text>
            <CodiItemImg
                source={{uri: codiSetDetail.img}}
            />
            <TouchableWithoutFeedback onPress={changeHeart}>
                <TextContainer>
                    <Text>{itemLike.liked ? '❤️' : '💜'}{ itemLike.likes }</Text>
                </TextContainer>
            </TouchableWithoutFeedback>
            <Text>
                {codiSetDetail.content}
            </Text>
            <ScrollView>
                {codiSetDetail.items.map(item => {
                    if (Object.keys(item).length !== 0) {
                        return (
                            <TouchableWithoutFeedback
                            style={{marginBottom: 5}}
                            key={item.id}
                            onPress={() => {
                                navigation.navigate('WebView', { url: item.url })
                            }}>
                                <ItemContainer>
                                    <Text style={{fontWeight: 'bold'}}>{item.category}</Text>
                                    <Text>{item.name}</Text>
                                    <Text>{item.price} 원</Text>
                                </ItemContainer>
                            </TouchableWithoutFeedback>
                        )
                    } else {
                        nullCount++;
                    }
                })}
                {nullCount === 5 ? <Text>등록된 상품의 정보가 없어요</Text> : null}
            </ScrollView>
        </Container>
    )
}

export default CodiDetailScreen;