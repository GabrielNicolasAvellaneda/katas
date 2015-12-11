package com.kata
/**
 * Created by developer on 11/12/2015.
 */

object MorseCodeDecoder {

  sealed trait Tree[A] {
    def value: A
    def left: Option[Tree[A]]
    def right: Option[Tree[A]]
  }

  case class TreeNode (value:Char, left: Option[TreeNode], right: Option[TreeNode]) extends Tree[Char] {
  }

  def navigateByMorseChar(node: TreeNode, morseChar:Char) = morseChar match {
    case '.' => node.left
    case '-' => node.right
  }

  def decode(morseCode: String) : String = {
    val root = TreeNode('\0', Some(TreeNode('E', None, Some(TreeNode('A', None, None)))), Some(TreeNode('T', None, None)))
    var (result, morseCodeRest) = decodeChar(root, morseCode)
    while (!morseCodeRest.isEmpty) {
      if (morseCodeRest.startsWith("   ")) {
        morseCodeRest = morseCodeRest.substring(3)
        result = result + " "
      } else {
        morseCodeRest = morseCodeRest.substring(1)
      }
      val (moreDecoded, rest) = decodeChar(root, morseCodeRest)
      result = result + moreDecoded
      morseCodeRest = rest
    }
    result
  }

  def decodeChar(node:TreeNode, morseCode:String) : (String, String) = {
    if (morseCode.isEmpty || morseCode(0) == ' ') {
      (node.value.toString, morseCode)
    }
    else {
      val char = morseCode(0)
      val branch = navigateByMorseChar(node, char).get
      decodeChar(branch, morseCode.substring(1))
    }
 }
}
