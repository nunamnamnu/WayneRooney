import streamlit as st
from PIL import Image
import pandas as pd
import csv
st.markdown('<center><h1 class="big-font"><font color="darkblue">huyền thoại bóng đá:<br> Wayne Rooney</center></h1>', unsafe_allow_html=True)
st.markdown('\n')
st.image('picture/rooney-1.jpg', width=700)

cauthu=pd.read_excel("cup.xlsx")
cauthu.to_csv("cup.csv")
cau_thu=pd.read_csv("cup.csv",index_col=0)

cols=st.columns(2)
cols[0].image(Image.open('picture/Rooney2.jpg'))
cols[1].write('''<b>Wayne Rooney</b> là một cầu thủ bóng đá nổi tiếng người <b>Anh</b>, sinh ngày <b>24 tháng 10 năm 1985</b> tại <b>Liverpool, Anh</b>.<br>    
   Anh được biết đến là một trong những <b>tiền đạo xuất sắc nhất của thế hệ của mình</b> và đã góp phần quan trọng trong nhiều thành công của đội tuyển Anh và câu lạc bộ mà anh đã thi đấu.
''',unsafe_allow_html=True)

cols=st.columns(2)
cols[1].image(Image.open('picture/rooney4.jpg'))
cols[0].write('''
Rooney bắt đầu sự nghiệp chuyên nghiệp của mình tại <b>Everton</b>,
một câu lạc bộ bóng đá ở thành phố quê hương của anh.
Anh đã nhanh chóng thu hút sự chú ý của giới chuyên môn và trở thành một trong những tài năng trẻ triển vọng nhất của bóng đá Anh. 
Với Everton, anh đã ghi được nhiều bàn thắng ấn tượng và được coi là một trong những cầu thủ trẻ xuất sắc nhất ở nước Anh.
''',unsafe_allow_html=True)

cols=st.columns(2)
cols[0].image(Image.open('picture/rooney3.jpg'))
cols[1].write('''Sau đó, vào năm <b>2004</b>, Rooney chuyển đến câu lạc bộ <b>Manchester United</b> - một trong những câu lạc bộ lớn nhất và thành công nhất ở Anh.
 Tại Manchester United, anh đã trở thành một huyền thoại của câu lạc bộ và giành được nhiều danh hiệu quan trọng. 
Anh đã giúp Manchester United giành được nhiều <b>chức vô địch Premier League, FA Cup, League Cup và UEFA Champions League. </b>
Rooney đã ghi tổng cộng <b>253 bàn thắng</b> cho Manchester United, vượt qua kỷ lục ghi bàn của Sir Bobby Charlton để trở thành <b>cầu thủ ghi bàn nhiều nhất</b> trong lịch sử câu lạc bộ.''',unsafe_allow_html=True)
with st.expander("Xem thêm"):
    st.write("""Ngoài ra, Rooney cũng là một thành viên quan trọng của đội tuyển quốc gia Anh. 
    Anh đã thi đấu cho đội tuyển Anh trong nhiều kỳ World Cup và Euro và là một trong những cầu thủ quan trọng nhất trong lịch sử đội tuyển. 
    Rooney đã ghi được <b>53 bàn thắng</b> trong <b>120 trận đấu</b> cho đội tuyển Anh, trở thành cầu thủ ghi bàn nhiều thứ hai trong lịch sử đội tuyển sau Bobby Charlton.""",unsafe_allow_html=True)
    st.image(Image.open('picture/rooney6.jpg'))

cols=st.columns(2)
cols[1].image(Image.open('picture/rooney4.jpg'))
cols[0].write('''Sự nghiệp của Rooney không chỉ nổi tiếng với khả năng ghi bàn xuất sắc mà anh còn được biết đến với sự cống hiến, sự quyết tâm và tinh thần lãnh đạo. 
Rooney là một <b>cầu thủ đa năng</b> có khả năng chơi ở nhiều vị trí khác nhau trong hàng công, từ tiền đạo cắm đến tiền đạo cánh.''',unsafe_allow_html=True)
with st.expander("Thành tích"):
    st.write("Xem thêm về thành tích của huyền thoại Wayne Rooney")
    st.dataframe(cau_thu)

cols=st.columns(2)
cols[0].image(Image.open('picture/rooney5.jpg'))
cols[1].write("Sau khi rời Manchester United, Rooney đã chơi cho một số câu lạc bộ khác như <b>Everton, D.C. United ở Mỹ và Derby County</b>, nơi anh đã cũng đã <b>kết thúc sự nghiệp cầu thủ của mình vào năm 2021</b>.",unsafe_allow_html=True)

st.image('picture/rooney7.jpg',width=700)
st.write('''Wayne Rooney là một huyền thoại của bóng đá Anh, người đã để lại dấu ấn sâu sắc trong lịch sử của câu lạc bộ và đội tuyển quốc gia. 
Anh được công nhận với tài năng và thành tích đáng kinh ngạc và sẽ mãi mãi được nhớ đến như một trong những cầu thủ <b>vĩ đại nhất</b> trong thế hệ của mình.''',unsafe_allow_html=True)