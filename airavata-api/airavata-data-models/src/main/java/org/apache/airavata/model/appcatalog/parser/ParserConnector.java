/**
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

/**
 * Autogenerated by Thrift Compiler (0.10.0)
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */
package org.apache.airavata.model.appcatalog.parser;

@SuppressWarnings({"cast", "rawtypes", "serial", "unchecked", "unused"})
@javax.annotation.Generated(value = "Autogenerated by Thrift Compiler (0.10.0)")
public class ParserConnector implements org.apache.thrift.TBase<ParserConnector, ParserConnector._Fields>, java.io.Serializable, Cloneable, Comparable<ParserConnector> {
  private static final org.apache.thrift.protocol.TStruct STRUCT_DESC = new org.apache.thrift.protocol.TStruct("ParserConnector");

  private static final org.apache.thrift.protocol.TField ID_FIELD_DESC = new org.apache.thrift.protocol.TField("id", org.apache.thrift.protocol.TType.STRING, (short)1);
  private static final org.apache.thrift.protocol.TField PARENT_PARSER_ID_FIELD_DESC = new org.apache.thrift.protocol.TField("parentParserId", org.apache.thrift.protocol.TType.STRING, (short)2);
  private static final org.apache.thrift.protocol.TField CHILD_PARSER_ID_FIELD_DESC = new org.apache.thrift.protocol.TField("childParserId", org.apache.thrift.protocol.TType.STRING, (short)3);
  private static final org.apache.thrift.protocol.TField CONNECTOR_INPUTS_FIELD_DESC = new org.apache.thrift.protocol.TField("connectorInputs", org.apache.thrift.protocol.TType.LIST, (short)4);
  private static final org.apache.thrift.protocol.TField PARSING_TEMPLATE_ID_FIELD_DESC = new org.apache.thrift.protocol.TField("parsingTemplateId", org.apache.thrift.protocol.TType.STRING, (short)5);

  private static final org.apache.thrift.scheme.SchemeFactory STANDARD_SCHEME_FACTORY = new ParserConnectorStandardSchemeFactory();
  private static final org.apache.thrift.scheme.SchemeFactory TUPLE_SCHEME_FACTORY = new ParserConnectorTupleSchemeFactory();

  private java.lang.String id; // required
  private java.lang.String parentParserId; // required
  private java.lang.String childParserId; // required
  private java.util.List<ParserConnectorInput> connectorInputs; // required
  private java.lang.String parsingTemplateId; // required

  /** The set of fields this struct contains, along with convenience methods for finding and manipulating them. */
  public enum _Fields implements org.apache.thrift.TFieldIdEnum {
    ID((short)1, "id"),
    PARENT_PARSER_ID((short)2, "parentParserId"),
    CHILD_PARSER_ID((short)3, "childParserId"),
    CONNECTOR_INPUTS((short)4, "connectorInputs"),
    PARSING_TEMPLATE_ID((short)5, "parsingTemplateId");

    private static final java.util.Map<java.lang.String, _Fields> byName = new java.util.HashMap<java.lang.String, _Fields>();

    static {
      for (_Fields field : java.util.EnumSet.allOf(_Fields.class)) {
        byName.put(field.getFieldName(), field);
      }
    }

    /**
     * Find the _Fields constant that matches fieldId, or null if its not found.
     */
    public static _Fields findByThriftId(int fieldId) {
      switch(fieldId) {
        case 1: // ID
          return ID;
        case 2: // PARENT_PARSER_ID
          return PARENT_PARSER_ID;
        case 3: // CHILD_PARSER_ID
          return CHILD_PARSER_ID;
        case 4: // CONNECTOR_INPUTS
          return CONNECTOR_INPUTS;
        case 5: // PARSING_TEMPLATE_ID
          return PARSING_TEMPLATE_ID;
        default:
          return null;
      }
    }

    /**
     * Find the _Fields constant that matches fieldId, throwing an exception
     * if it is not found.
     */
    public static _Fields findByThriftIdOrThrow(int fieldId) {
      _Fields fields = findByThriftId(fieldId);
      if (fields == null) throw new java.lang.IllegalArgumentException("Field " + fieldId + " doesn't exist!");
      return fields;
    }

    /**
     * Find the _Fields constant that matches name, or null if its not found.
     */
    public static _Fields findByName(java.lang.String name) {
      return byName.get(name);
    }

    private final short _thriftId;
    private final java.lang.String _fieldName;

    _Fields(short thriftId, java.lang.String fieldName) {
      _thriftId = thriftId;
      _fieldName = fieldName;
    }

    public short getThriftFieldId() {
      return _thriftId;
    }

    public java.lang.String getFieldName() {
      return _fieldName;
    }
  }

  // isset id assignments
  public static final java.util.Map<_Fields, org.apache.thrift.meta_data.FieldMetaData> metaDataMap;
  static {
    java.util.Map<_Fields, org.apache.thrift.meta_data.FieldMetaData> tmpMap = new java.util.EnumMap<_Fields, org.apache.thrift.meta_data.FieldMetaData>(_Fields.class);
    tmpMap.put(_Fields.ID, new org.apache.thrift.meta_data.FieldMetaData("id", org.apache.thrift.TFieldRequirementType.REQUIRED, 
        new org.apache.thrift.meta_data.FieldValueMetaData(org.apache.thrift.protocol.TType.STRING)));
    tmpMap.put(_Fields.PARENT_PARSER_ID, new org.apache.thrift.meta_data.FieldMetaData("parentParserId", org.apache.thrift.TFieldRequirementType.REQUIRED, 
        new org.apache.thrift.meta_data.FieldValueMetaData(org.apache.thrift.protocol.TType.STRING)));
    tmpMap.put(_Fields.CHILD_PARSER_ID, new org.apache.thrift.meta_data.FieldMetaData("childParserId", org.apache.thrift.TFieldRequirementType.REQUIRED, 
        new org.apache.thrift.meta_data.FieldValueMetaData(org.apache.thrift.protocol.TType.STRING)));
    tmpMap.put(_Fields.CONNECTOR_INPUTS, new org.apache.thrift.meta_data.FieldMetaData("connectorInputs", org.apache.thrift.TFieldRequirementType.REQUIRED, 
        new org.apache.thrift.meta_data.ListMetaData(org.apache.thrift.protocol.TType.LIST, 
            new org.apache.thrift.meta_data.StructMetaData(org.apache.thrift.protocol.TType.STRUCT, ParserConnectorInput.class))));
    tmpMap.put(_Fields.PARSING_TEMPLATE_ID, new org.apache.thrift.meta_data.FieldMetaData("parsingTemplateId", org.apache.thrift.TFieldRequirementType.REQUIRED, 
        new org.apache.thrift.meta_data.FieldValueMetaData(org.apache.thrift.protocol.TType.STRING)));
    metaDataMap = java.util.Collections.unmodifiableMap(tmpMap);
    org.apache.thrift.meta_data.FieldMetaData.addStructMetaDataMap(ParserConnector.class, metaDataMap);
  }

  public ParserConnector() {
  }

  public ParserConnector(
    java.lang.String id,
    java.lang.String parentParserId,
    java.lang.String childParserId,
    java.util.List<ParserConnectorInput> connectorInputs,
    java.lang.String parsingTemplateId)
  {
    this();
    this.id = id;
    this.parentParserId = parentParserId;
    this.childParserId = childParserId;
    this.connectorInputs = connectorInputs;
    this.parsingTemplateId = parsingTemplateId;
  }

  /**
   * Performs a deep copy on <i>other</i>.
   */
  public ParserConnector(ParserConnector other) {
    if (other.isSetId()) {
      this.id = other.id;
    }
    if (other.isSetParentParserId()) {
      this.parentParserId = other.parentParserId;
    }
    if (other.isSetChildParserId()) {
      this.childParserId = other.childParserId;
    }
    if (other.isSetConnectorInputs()) {
      java.util.List<ParserConnectorInput> __this__connectorInputs = new java.util.ArrayList<ParserConnectorInput>(other.connectorInputs.size());
      for (ParserConnectorInput other_element : other.connectorInputs) {
        __this__connectorInputs.add(new ParserConnectorInput(other_element));
      }
      this.connectorInputs = __this__connectorInputs;
    }
    if (other.isSetParsingTemplateId()) {
      this.parsingTemplateId = other.parsingTemplateId;
    }
  }

  public ParserConnector deepCopy() {
    return new ParserConnector(this);
  }

  @Override
  public void clear() {
    this.id = null;
    this.parentParserId = null;
    this.childParserId = null;
    this.connectorInputs = null;
    this.parsingTemplateId = null;
  }

  public java.lang.String getId() {
    return this.id;
  }

  public void setId(java.lang.String id) {
    this.id = id;
  }

  public void unsetId() {
    this.id = null;
  }

  /** Returns true if field id is set (has been assigned a value) and false otherwise */
  public boolean isSetId() {
    return this.id != null;
  }

  public void setIdIsSet(boolean value) {
    if (!value) {
      this.id = null;
    }
  }

  public java.lang.String getParentParserId() {
    return this.parentParserId;
  }

  public void setParentParserId(java.lang.String parentParserId) {
    this.parentParserId = parentParserId;
  }

  public void unsetParentParserId() {
    this.parentParserId = null;
  }

  /** Returns true if field parentParserId is set (has been assigned a value) and false otherwise */
  public boolean isSetParentParserId() {
    return this.parentParserId != null;
  }

  public void setParentParserIdIsSet(boolean value) {
    if (!value) {
      this.parentParserId = null;
    }
  }

  public java.lang.String getChildParserId() {
    return this.childParserId;
  }

  public void setChildParserId(java.lang.String childParserId) {
    this.childParserId = childParserId;
  }

  public void unsetChildParserId() {
    this.childParserId = null;
  }

  /** Returns true if field childParserId is set (has been assigned a value) and false otherwise */
  public boolean isSetChildParserId() {
    return this.childParserId != null;
  }

  public void setChildParserIdIsSet(boolean value) {
    if (!value) {
      this.childParserId = null;
    }
  }

  public int getConnectorInputsSize() {
    return (this.connectorInputs == null) ? 0 : this.connectorInputs.size();
  }

  public java.util.Iterator<ParserConnectorInput> getConnectorInputsIterator() {
    return (this.connectorInputs == null) ? null : this.connectorInputs.iterator();
  }

  public void addToConnectorInputs(ParserConnectorInput elem) {
    if (this.connectorInputs == null) {
      this.connectorInputs = new java.util.ArrayList<ParserConnectorInput>();
    }
    this.connectorInputs.add(elem);
  }

  public java.util.List<ParserConnectorInput> getConnectorInputs() {
    return this.connectorInputs;
  }

  public void setConnectorInputs(java.util.List<ParserConnectorInput> connectorInputs) {
    this.connectorInputs = connectorInputs;
  }

  public void unsetConnectorInputs() {
    this.connectorInputs = null;
  }

  /** Returns true if field connectorInputs is set (has been assigned a value) and false otherwise */
  public boolean isSetConnectorInputs() {
    return this.connectorInputs != null;
  }

  public void setConnectorInputsIsSet(boolean value) {
    if (!value) {
      this.connectorInputs = null;
    }
  }

  public java.lang.String getParsingTemplateId() {
    return this.parsingTemplateId;
  }

  public void setParsingTemplateId(java.lang.String parsingTemplateId) {
    this.parsingTemplateId = parsingTemplateId;
  }

  public void unsetParsingTemplateId() {
    this.parsingTemplateId = null;
  }

  /** Returns true if field parsingTemplateId is set (has been assigned a value) and false otherwise */
  public boolean isSetParsingTemplateId() {
    return this.parsingTemplateId != null;
  }

  public void setParsingTemplateIdIsSet(boolean value) {
    if (!value) {
      this.parsingTemplateId = null;
    }
  }

  public void setFieldValue(_Fields field, java.lang.Object value) {
    switch (field) {
    case ID:
      if (value == null) {
        unsetId();
      } else {
        setId((java.lang.String)value);
      }
      break;

    case PARENT_PARSER_ID:
      if (value == null) {
        unsetParentParserId();
      } else {
        setParentParserId((java.lang.String)value);
      }
      break;

    case CHILD_PARSER_ID:
      if (value == null) {
        unsetChildParserId();
      } else {
        setChildParserId((java.lang.String)value);
      }
      break;

    case CONNECTOR_INPUTS:
      if (value == null) {
        unsetConnectorInputs();
      } else {
        setConnectorInputs((java.util.List<ParserConnectorInput>)value);
      }
      break;

    case PARSING_TEMPLATE_ID:
      if (value == null) {
        unsetParsingTemplateId();
      } else {
        setParsingTemplateId((java.lang.String)value);
      }
      break;

    }
  }

  public java.lang.Object getFieldValue(_Fields field) {
    switch (field) {
    case ID:
      return getId();

    case PARENT_PARSER_ID:
      return getParentParserId();

    case CHILD_PARSER_ID:
      return getChildParserId();

    case CONNECTOR_INPUTS:
      return getConnectorInputs();

    case PARSING_TEMPLATE_ID:
      return getParsingTemplateId();

    }
    throw new java.lang.IllegalStateException();
  }

  /** Returns true if field corresponding to fieldID is set (has been assigned a value) and false otherwise */
  public boolean isSet(_Fields field) {
    if (field == null) {
      throw new java.lang.IllegalArgumentException();
    }

    switch (field) {
    case ID:
      return isSetId();
    case PARENT_PARSER_ID:
      return isSetParentParserId();
    case CHILD_PARSER_ID:
      return isSetChildParserId();
    case CONNECTOR_INPUTS:
      return isSetConnectorInputs();
    case PARSING_TEMPLATE_ID:
      return isSetParsingTemplateId();
    }
    throw new java.lang.IllegalStateException();
  }

  @Override
  public boolean equals(java.lang.Object that) {
    if (that == null)
      return false;
    if (that instanceof ParserConnector)
      return this.equals((ParserConnector)that);
    return false;
  }

  public boolean equals(ParserConnector that) {
    if (that == null)
      return false;
    if (this == that)
      return true;

    boolean this_present_id = true && this.isSetId();
    boolean that_present_id = true && that.isSetId();
    if (this_present_id || that_present_id) {
      if (!(this_present_id && that_present_id))
        return false;
      if (!this.id.equals(that.id))
        return false;
    }

    boolean this_present_parentParserId = true && this.isSetParentParserId();
    boolean that_present_parentParserId = true && that.isSetParentParserId();
    if (this_present_parentParserId || that_present_parentParserId) {
      if (!(this_present_parentParserId && that_present_parentParserId))
        return false;
      if (!this.parentParserId.equals(that.parentParserId))
        return false;
    }

    boolean this_present_childParserId = true && this.isSetChildParserId();
    boolean that_present_childParserId = true && that.isSetChildParserId();
    if (this_present_childParserId || that_present_childParserId) {
      if (!(this_present_childParserId && that_present_childParserId))
        return false;
      if (!this.childParserId.equals(that.childParserId))
        return false;
    }

    boolean this_present_connectorInputs = true && this.isSetConnectorInputs();
    boolean that_present_connectorInputs = true && that.isSetConnectorInputs();
    if (this_present_connectorInputs || that_present_connectorInputs) {
      if (!(this_present_connectorInputs && that_present_connectorInputs))
        return false;
      if (!this.connectorInputs.equals(that.connectorInputs))
        return false;
    }

    boolean this_present_parsingTemplateId = true && this.isSetParsingTemplateId();
    boolean that_present_parsingTemplateId = true && that.isSetParsingTemplateId();
    if (this_present_parsingTemplateId || that_present_parsingTemplateId) {
      if (!(this_present_parsingTemplateId && that_present_parsingTemplateId))
        return false;
      if (!this.parsingTemplateId.equals(that.parsingTemplateId))
        return false;
    }

    return true;
  }

  @Override
  public int hashCode() {
    int hashCode = 1;

    hashCode = hashCode * 8191 + ((isSetId()) ? 131071 : 524287);
    if (isSetId())
      hashCode = hashCode * 8191 + id.hashCode();

    hashCode = hashCode * 8191 + ((isSetParentParserId()) ? 131071 : 524287);
    if (isSetParentParserId())
      hashCode = hashCode * 8191 + parentParserId.hashCode();

    hashCode = hashCode * 8191 + ((isSetChildParserId()) ? 131071 : 524287);
    if (isSetChildParserId())
      hashCode = hashCode * 8191 + childParserId.hashCode();

    hashCode = hashCode * 8191 + ((isSetConnectorInputs()) ? 131071 : 524287);
    if (isSetConnectorInputs())
      hashCode = hashCode * 8191 + connectorInputs.hashCode();

    hashCode = hashCode * 8191 + ((isSetParsingTemplateId()) ? 131071 : 524287);
    if (isSetParsingTemplateId())
      hashCode = hashCode * 8191 + parsingTemplateId.hashCode();

    return hashCode;
  }

  @Override
  public int compareTo(ParserConnector other) {
    if (!getClass().equals(other.getClass())) {
      return getClass().getName().compareTo(other.getClass().getName());
    }

    int lastComparison = 0;

    lastComparison = java.lang.Boolean.valueOf(isSetId()).compareTo(other.isSetId());
    if (lastComparison != 0) {
      return lastComparison;
    }
    if (isSetId()) {
      lastComparison = org.apache.thrift.TBaseHelper.compareTo(this.id, other.id);
      if (lastComparison != 0) {
        return lastComparison;
      }
    }
    lastComparison = java.lang.Boolean.valueOf(isSetParentParserId()).compareTo(other.isSetParentParserId());
    if (lastComparison != 0) {
      return lastComparison;
    }
    if (isSetParentParserId()) {
      lastComparison = org.apache.thrift.TBaseHelper.compareTo(this.parentParserId, other.parentParserId);
      if (lastComparison != 0) {
        return lastComparison;
      }
    }
    lastComparison = java.lang.Boolean.valueOf(isSetChildParserId()).compareTo(other.isSetChildParserId());
    if (lastComparison != 0) {
      return lastComparison;
    }
    if (isSetChildParserId()) {
      lastComparison = org.apache.thrift.TBaseHelper.compareTo(this.childParserId, other.childParserId);
      if (lastComparison != 0) {
        return lastComparison;
      }
    }
    lastComparison = java.lang.Boolean.valueOf(isSetConnectorInputs()).compareTo(other.isSetConnectorInputs());
    if (lastComparison != 0) {
      return lastComparison;
    }
    if (isSetConnectorInputs()) {
      lastComparison = org.apache.thrift.TBaseHelper.compareTo(this.connectorInputs, other.connectorInputs);
      if (lastComparison != 0) {
        return lastComparison;
      }
    }
    lastComparison = java.lang.Boolean.valueOf(isSetParsingTemplateId()).compareTo(other.isSetParsingTemplateId());
    if (lastComparison != 0) {
      return lastComparison;
    }
    if (isSetParsingTemplateId()) {
      lastComparison = org.apache.thrift.TBaseHelper.compareTo(this.parsingTemplateId, other.parsingTemplateId);
      if (lastComparison != 0) {
        return lastComparison;
      }
    }
    return 0;
  }

  public _Fields fieldForId(int fieldId) {
    return _Fields.findByThriftId(fieldId);
  }

  public void read(org.apache.thrift.protocol.TProtocol iprot) throws org.apache.thrift.TException {
    scheme(iprot).read(iprot, this);
  }

  public void write(org.apache.thrift.protocol.TProtocol oprot) throws org.apache.thrift.TException {
    scheme(oprot).write(oprot, this);
  }

  @Override
  public java.lang.String toString() {
    java.lang.StringBuilder sb = new java.lang.StringBuilder("ParserConnector(");
    boolean first = true;

    sb.append("id:");
    if (this.id == null) {
      sb.append("null");
    } else {
      sb.append(this.id);
    }
    first = false;
    if (!first) sb.append(", ");
    sb.append("parentParserId:");
    if (this.parentParserId == null) {
      sb.append("null");
    } else {
      sb.append(this.parentParserId);
    }
    first = false;
    if (!first) sb.append(", ");
    sb.append("childParserId:");
    if (this.childParserId == null) {
      sb.append("null");
    } else {
      sb.append(this.childParserId);
    }
    first = false;
    if (!first) sb.append(", ");
    sb.append("connectorInputs:");
    if (this.connectorInputs == null) {
      sb.append("null");
    } else {
      sb.append(this.connectorInputs);
    }
    first = false;
    if (!first) sb.append(", ");
    sb.append("parsingTemplateId:");
    if (this.parsingTemplateId == null) {
      sb.append("null");
    } else {
      sb.append(this.parsingTemplateId);
    }
    first = false;
    sb.append(")");
    return sb.toString();
  }

  public void validate() throws org.apache.thrift.TException {
    // check for required fields
    if (!isSetId()) {
      throw new org.apache.thrift.protocol.TProtocolException("Required field 'id' is unset! Struct:" + toString());
    }

    if (!isSetParentParserId()) {
      throw new org.apache.thrift.protocol.TProtocolException("Required field 'parentParserId' is unset! Struct:" + toString());
    }

    if (!isSetChildParserId()) {
      throw new org.apache.thrift.protocol.TProtocolException("Required field 'childParserId' is unset! Struct:" + toString());
    }

    if (!isSetConnectorInputs()) {
      throw new org.apache.thrift.protocol.TProtocolException("Required field 'connectorInputs' is unset! Struct:" + toString());
    }

    if (!isSetParsingTemplateId()) {
      throw new org.apache.thrift.protocol.TProtocolException("Required field 'parsingTemplateId' is unset! Struct:" + toString());
    }

    // check for sub-struct validity
  }

  private void writeObject(java.io.ObjectOutputStream out) throws java.io.IOException {
    try {
      write(new org.apache.thrift.protocol.TCompactProtocol(new org.apache.thrift.transport.TIOStreamTransport(out)));
    } catch (org.apache.thrift.TException te) {
      throw new java.io.IOException(te);
    }
  }

  private void readObject(java.io.ObjectInputStream in) throws java.io.IOException, java.lang.ClassNotFoundException {
    try {
      read(new org.apache.thrift.protocol.TCompactProtocol(new org.apache.thrift.transport.TIOStreamTransport(in)));
    } catch (org.apache.thrift.TException te) {
      throw new java.io.IOException(te);
    }
  }

  private static class ParserConnectorStandardSchemeFactory implements org.apache.thrift.scheme.SchemeFactory {
    public ParserConnectorStandardScheme getScheme() {
      return new ParserConnectorStandardScheme();
    }
  }

  private static class ParserConnectorStandardScheme extends org.apache.thrift.scheme.StandardScheme<ParserConnector> {

    public void read(org.apache.thrift.protocol.TProtocol iprot, ParserConnector struct) throws org.apache.thrift.TException {
      org.apache.thrift.protocol.TField schemeField;
      iprot.readStructBegin();
      while (true)
      {
        schemeField = iprot.readFieldBegin();
        if (schemeField.type == org.apache.thrift.protocol.TType.STOP) { 
          break;
        }
        switch (schemeField.id) {
          case 1: // ID
            if (schemeField.type == org.apache.thrift.protocol.TType.STRING) {
              struct.id = iprot.readString();
              struct.setIdIsSet(true);
            } else { 
              org.apache.thrift.protocol.TProtocolUtil.skip(iprot, schemeField.type);
            }
            break;
          case 2: // PARENT_PARSER_ID
            if (schemeField.type == org.apache.thrift.protocol.TType.STRING) {
              struct.parentParserId = iprot.readString();
              struct.setParentParserIdIsSet(true);
            } else { 
              org.apache.thrift.protocol.TProtocolUtil.skip(iprot, schemeField.type);
            }
            break;
          case 3: // CHILD_PARSER_ID
            if (schemeField.type == org.apache.thrift.protocol.TType.STRING) {
              struct.childParserId = iprot.readString();
              struct.setChildParserIdIsSet(true);
            } else { 
              org.apache.thrift.protocol.TProtocolUtil.skip(iprot, schemeField.type);
            }
            break;
          case 4: // CONNECTOR_INPUTS
            if (schemeField.type == org.apache.thrift.protocol.TType.LIST) {
              {
                org.apache.thrift.protocol.TList _list16 = iprot.readListBegin();
                struct.connectorInputs = new java.util.ArrayList<ParserConnectorInput>(_list16.size);
                ParserConnectorInput _elem17;
                for (int _i18 = 0; _i18 < _list16.size; ++_i18)
                {
                  _elem17 = new ParserConnectorInput();
                  _elem17.read(iprot);
                  struct.connectorInputs.add(_elem17);
                }
                iprot.readListEnd();
              }
              struct.setConnectorInputsIsSet(true);
            } else { 
              org.apache.thrift.protocol.TProtocolUtil.skip(iprot, schemeField.type);
            }
            break;
          case 5: // PARSING_TEMPLATE_ID
            if (schemeField.type == org.apache.thrift.protocol.TType.STRING) {
              struct.parsingTemplateId = iprot.readString();
              struct.setParsingTemplateIdIsSet(true);
            } else { 
              org.apache.thrift.protocol.TProtocolUtil.skip(iprot, schemeField.type);
            }
            break;
          default:
            org.apache.thrift.protocol.TProtocolUtil.skip(iprot, schemeField.type);
        }
        iprot.readFieldEnd();
      }
      iprot.readStructEnd();
      struct.validate();
    }

    public void write(org.apache.thrift.protocol.TProtocol oprot, ParserConnector struct) throws org.apache.thrift.TException {
      struct.validate();

      oprot.writeStructBegin(STRUCT_DESC);
      if (struct.id != null) {
        oprot.writeFieldBegin(ID_FIELD_DESC);
        oprot.writeString(struct.id);
        oprot.writeFieldEnd();
      }
      if (struct.parentParserId != null) {
        oprot.writeFieldBegin(PARENT_PARSER_ID_FIELD_DESC);
        oprot.writeString(struct.parentParserId);
        oprot.writeFieldEnd();
      }
      if (struct.childParserId != null) {
        oprot.writeFieldBegin(CHILD_PARSER_ID_FIELD_DESC);
        oprot.writeString(struct.childParserId);
        oprot.writeFieldEnd();
      }
      if (struct.connectorInputs != null) {
        oprot.writeFieldBegin(CONNECTOR_INPUTS_FIELD_DESC);
        {
          oprot.writeListBegin(new org.apache.thrift.protocol.TList(org.apache.thrift.protocol.TType.STRUCT, struct.connectorInputs.size()));
          for (ParserConnectorInput _iter19 : struct.connectorInputs)
          {
            _iter19.write(oprot);
          }
          oprot.writeListEnd();
        }
        oprot.writeFieldEnd();
      }
      if (struct.parsingTemplateId != null) {
        oprot.writeFieldBegin(PARSING_TEMPLATE_ID_FIELD_DESC);
        oprot.writeString(struct.parsingTemplateId);
        oprot.writeFieldEnd();
      }
      oprot.writeFieldStop();
      oprot.writeStructEnd();
    }

  }

  private static class ParserConnectorTupleSchemeFactory implements org.apache.thrift.scheme.SchemeFactory {
    public ParserConnectorTupleScheme getScheme() {
      return new ParserConnectorTupleScheme();
    }
  }

  private static class ParserConnectorTupleScheme extends org.apache.thrift.scheme.TupleScheme<ParserConnector> {

    @Override
    public void write(org.apache.thrift.protocol.TProtocol prot, ParserConnector struct) throws org.apache.thrift.TException {
      org.apache.thrift.protocol.TTupleProtocol oprot = (org.apache.thrift.protocol.TTupleProtocol) prot;
      oprot.writeString(struct.id);
      oprot.writeString(struct.parentParserId);
      oprot.writeString(struct.childParserId);
      {
        oprot.writeI32(struct.connectorInputs.size());
        for (ParserConnectorInput _iter20 : struct.connectorInputs)
        {
          _iter20.write(oprot);
        }
      }
      oprot.writeString(struct.parsingTemplateId);
    }

    @Override
    public void read(org.apache.thrift.protocol.TProtocol prot, ParserConnector struct) throws org.apache.thrift.TException {
      org.apache.thrift.protocol.TTupleProtocol iprot = (org.apache.thrift.protocol.TTupleProtocol) prot;
      struct.id = iprot.readString();
      struct.setIdIsSet(true);
      struct.parentParserId = iprot.readString();
      struct.setParentParserIdIsSet(true);
      struct.childParserId = iprot.readString();
      struct.setChildParserIdIsSet(true);
      {
        org.apache.thrift.protocol.TList _list21 = new org.apache.thrift.protocol.TList(org.apache.thrift.protocol.TType.STRUCT, iprot.readI32());
        struct.connectorInputs = new java.util.ArrayList<ParserConnectorInput>(_list21.size);
        ParserConnectorInput _elem22;
        for (int _i23 = 0; _i23 < _list21.size; ++_i23)
        {
          _elem22 = new ParserConnectorInput();
          _elem22.read(iprot);
          struct.connectorInputs.add(_elem22);
        }
      }
      struct.setConnectorInputsIsSet(true);
      struct.parsingTemplateId = iprot.readString();
      struct.setParsingTemplateIdIsSet(true);
    }
  }

  private static <S extends org.apache.thrift.scheme.IScheme> S scheme(org.apache.thrift.protocol.TProtocol proto) {
    return (org.apache.thrift.scheme.StandardScheme.class.equals(proto.getScheme()) ? STANDARD_SCHEME_FACTORY : TUPLE_SCHEME_FACTORY).getScheme();
  }
}

