import com.kata.MorseCodeDecoder
import org.scalatest.{Matchers, FlatSpec}

/**
 * Created by developer on 11/12/2015.
 */
class MorseCodeDecoderSpec extends FlatSpec with Matchers {

  "MorseCodeDecoder" should "decode a single character" in {

    MorseCodeDecoder.decode(".") should === ("E")
    MorseCodeDecoder.decode("-") should === ("T")
  }
}
