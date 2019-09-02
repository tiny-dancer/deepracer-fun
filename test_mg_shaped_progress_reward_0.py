import pytest
import os

from mg_shaped_progress_reward_0 import reward_function


@pytest.mark.parametrize("progress,expected", [(51.94621350637277, 8), (1, 6), (30, 42), (81, 42), (92, 42), (100, 42)])
def test_reward_function(progress,expected):
    os.environ['LOCAL_TESTING'] = 'true'

    params = {
        'all_wheels_on_track': 1,
        'waypoints': [[6.309836387634277,2.717386484146118],[6.195788621902466,2.7166789770126343],[6.081685543060303,2.715367913246155],[5.967700958251953,2.7118070125579834],[5.85396146774292,2.704580545425415],[5.740401983261108,2.6932029724121094],[5.627721548080444,2.675312042236328],[5.5175135135650635,2.6464585065841675],[5.409301042556763,2.609961986541748],[5.301126956939697,2.574303984642029],[5.1921679973602295,2.541111946105957],[5.0821373462677,2.5100131034851074],[4.970782518386841,2.4851750135421753],[4.8580474853515625,2.4710450172424316],[4.744303464889526,2.4700599908828735],[4.630417108535767,2.481245994567871],[4.5177764892578125,2.499838948249817],[4.407072305679321,2.5253244638442993],[4.298267602920532,2.559592604637146],[4.190068483352661,2.5966734886169434],[4.080982565879822,2.629265546798706],[3.970926523208618,2.6589781045913696],[3.859932541847229,2.686348557472229],[3.7475284337997437,2.7046855688095093],[3.633828043937683,2.7119990587234497],[3.5197654962539673,2.7135950326919556],[3.4057350158691406,2.713532567024231],[3.4057350158691406,2.713532567024231],[3.291683554649353,2.7141895294189453],[3.1491129398345947,2.7152745723724365],[3.0065420866012573,2.71635901927948],[2.863971471786499,2.7174439430236816],[2.7214009761810303,2.7185285091400146],[2.607404947280884,2.7163679599761963],[2.493346095085144,2.7110939025878906],[2.3756535053253174,2.696616053581238],[2.26602041721344,2.6667665243148804],[2.1631579995155334,2.6214065551757812],[2.0682084560394287,2.5637874603271484],[1.9771165251731873,2.4951614141464233],[1.8911914825439453,2.420231580734253],[1.8114585280418396,2.3387160301208496],[1.7394945025444033,2.250212073326111],[1.677141010761261,2.1548174619674683],[1.6248934864997864,2.0534849166870117],[1.5823744535446167,1.9477075338363647],[1.5505254864692688,1.8382489681243896],[1.5311545133590698,1.7257940173149109],[1.5271174907684326,1.6120454668998718],[1.539400041103363,1.4987789988517761],[1.5642725229263303,1.387354493141175],[1.5989729762077332,1.278760015964508],[1.6428920030593872,1.1736074686050415],[1.6964020133018494,1.0729964077472687],[1.7604795098304749,0.9785585701465607],[1.8357470035552979,0.8929627537727356],[1.9221299886703491,0.8187586665153503],[2.0174149870872498,0.7561855316162109],[2.1191929578781132,0.704834684729576],[2.22581148147583,0.6641798615455627],[2.33598256111145,0.635000690817833],[2.448741912841797,0.6194588989019394],[2.562835931777954,0.6146939992904663],[2.676932454109192,0.614323690533638],[2.790879011154175,0.615065410733223],[2.904958486557007,0.6154943406581879],[3.0190669298171997,0.6158859431743622],[3.1330950260162354,0.6165954917669296],[3.247138500213623,0.6172222346067429],[3.3612254858016968,0.6176614463329315],[3.475271463394165,0.6182866990566254],[3.5893020629882812,0.6188997328281403],[3.703405976295471,0.6189960688352585],[3.8174840211868286,0.6192460358142853],[3.9314393997192383,0.6201631426811218],[4.045536994934082,0.6195012480020523],[4.159003019332886,0.6116561591625214],[4.269382476806641,0.5892668068408966],[4.3730175495147705,0.5481619536876678],[4.465728044509888,0.4880164936184883],[4.5481369495391855,0.4090211018919938],[4.621875524520874,0.3185627665370703],[4.6936728954315186,0.22756083868443966],[4.7715795040130615,0.14663729816675186],[4.859802007675172,0.0780811086297031],[4.959166049957275,0.025352105498313904],[5.0663206577301025,-0.015855446457862854],[5.176241874694823,-0.05405664443969701],[5.283515930175781,-0.09862619638442993],[5.383999586105347,-0.15561671182513237],[5.4742419719696045,-0.22708586091175675],[5.549779891967773,-0.31260108947753906],[5.605553150177002,-0.40983645617961884],[5.639118432998657,-0.5152479559183121],[5.650930881500244,-0.6257368326187143],[5.643277406692505,-0.7384651899337769],[5.621659517288208,-0.8504203259944916],[5.592641115188599,-0.9608891308307648],[5.561022996902466,-1.070693016052246],[5.530486106872559,-1.1807215213775635],[5.5035319328308105,-1.2914490103721619],[5.480241298675537,-1.4030935168266296],[5.462010145187378,-1.5157455205917358],[5.45079493522644,-1.6292679905891418],[5.448741912841797,-1.7466390132904053],[5.459894418716431,-1.863289475440979],[5.48825740814209,-1.9755980372428894],[5.5363075733184814,-2.078725516796112],[5.60352635383606,-2.1696360111236572],[5.686964511871338,-2.2464959621429443],[5.7828369140625,-2.307755947113037],[5.88683295249939,-2.3526118993759155],[5.996015548706055,-2.380347967147827],[6.108441114425659,-2.3914250135421753],[6.2222607135772705,-2.388285517692566],[6.335166931152344,-2.371910572052002],[6.445005655288696,-2.3454989194869995],[6.550752639770508,-2.307651996612549],[6.655766487121582,-2.2621095180511475],[6.759855031967163,-2.215474545955658],[6.861518144607542,-2.164350986480714],[6.959713220596313,-2.106059551239014],[7.055949926376343,-2.044655501842499],[7.1512110233306885,-1.9823670387268066],[7.245310068130493,-1.9179010391235352],[7.3375091552734375,-1.8504455089569092],[7.42688202857971,-1.7797914743423473],[7.513786554336548,-1.7061240077018738],[7.5983476638793945,-1.6292839646339417],[7.677422523498535,-1.5470519661903381],[7.750153303146361,-1.457656025886537],[7.814417362213134,-1.3615394830703753],[7.8690268993377686,-1.2585055232048035],[7.910868167877197,-1.1510785222053528],[7.936350584030151,-1.041047990322113],[7.943183898925781,-0.9302619397640228],[7.929688930511475,-0.8188509643077873],[7.898606061935424,-0.7099088430404646],[7.858716964721679,-0.6015907526016219],[7.818351984024048,-0.49343155324459076],[7.785273790359497,-0.38304539024829865],[7.766066551208496,-0.2702548950910568],[7.764912366867065,-0.1569973491132242],[7.782723426818848,-0.04621594771742936],[7.816987752914428,0.06044381856918132],[7.862348318099976,0.1640622103586793],[7.9113850593566895,0.2672598920762539],[7.964816093444824,0.36797454953193665],[8.023759365081787,0.4654194712638855],[8.083719730377197,0.5625471323728577],[8.140750885009766,0.661509245634079],[8.19270658493042,0.7627629637718201],[8.238867044448853,0.8667940497398376],[8.279578924179077,0.9738516509532945],[8.31326961517334,1.0863134860992432],[8.33589792251587,1.2011854648590088],[8.344946384429932,1.3162800073623657],[8.336476802825928,1.4300925135612488],[8.307107925415039,1.5377934575080872],[8.256765365600586,1.6361489892005905],[8.187145233154297,1.7235015034675598],[8.102343559265135,1.7990955710411083],[8.010600328445433,1.8678620457649242],[7.919651508331299,1.9377470016479492],[7.838100910186769,2.0161675214767443],[7.767462730407714,2.1045645475387587],[7.704502820968628,2.199170470237732],[7.6444172859191895,2.2959940433502197],[7.5782294273376465,2.3898375034332275],[7.501000642776489,2.4726409912109375],[7.413156032562256,2.543642044067383],[7.317309379577637,2.601830005645752],[7.213808059692383,2.6475000381469727],[7.105192422866821,2.680868983268738],[6.993459939956665,2.7023710012435913],[6.879996061325073,2.7138789892196655],[6.766035556793213,2.718880534172058],[6.651995420455933,2.720201015472412],[6.537929534912109,2.7195639610290527],[6.423866033554077,2.7183064222335815],[6.309836387634277,2.717386484146118]],
        'closest_waypoints': [1, 2],
        'heading': -174.2816699776837,
        'is_left_of_center': 1,
        'is_reversed': 0,
        'progress': progress,
        'speed': 2.6666666666666665,
        'steering_angle': 9.999999999999998,
        'steps': 17,
        'track_width': 0.660273308091193,
        'x': 6.174768391459522,
        'y': 2.667314668352434
    }
    assert reward_function(params) > 0